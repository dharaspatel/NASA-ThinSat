# This script will use observed day and night length to update the forecasted
# latitude, longitude and altitude by performing a multiple regression on
# CHANGE in day length, night length and time of sunrise to the CHANGE in
# latitude, longitude and altitude.

# 0th report file uses Jack's initial conditions
# !! update changeinitcond.py

import os
import pdb
import sys
import pandas
import datetime
import fnmatch as fm
import numpy   as np
import matplotlib.pyplot as plt
from scipy.optimize          import curve_fit
import scipy.interpolate
from mpl_toolkits.mplot3d    import Axes3D
from statsmodels.api         import OLS
from statsmodels.stats.anova import anova_lm
import struct
# sys.path.insert(0, '/home/echickles/GMAT/R2018a/userfunctions/python')
import findjuliandates


source_dir = '../../Simulations/'
debug = False

DAY_LENGTH_THRESH = datetime.timedelta(seconds=60) # no day is this short
NIGHT_LENGTH_THRESH = datetime.timedelta(seconds=60) # no night is this short

NUM_SIMS = 101 # number of simulated mission variations
NUM_ORBITS = 80 # number of orbits to fit per simulation
NUM_SIM_DATA = 14400 # number of data in each simulation
NUM_PARAMS = 8 # the number of parameters to use to fit each orbit function

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

latitude = np.empty((NUM_SIMS, NUM_SIM_DATA)) # raw position data for each simulation
longitude = np.empty((NUM_SIMS, NUM_SIM_DATA))
altitude = np.empty((NUM_SIMS, NUM_SIM_DATA))
latitude_res = np.empty((NUM_SIMS, NUM_SIM_DATA)) # residual position data for each simulation
longitude_res = np.empty((NUM_SIMS, NUM_SIM_DATA))
altitude_res = np.empty((NUM_SIMS, NUM_SIM_DATA))
elapsed_secs = np.empty((NUM_SIMS, NUM_SIM_DATA)) # time vectors for each simulation
orbit_lengths = np.empty((NUM_SIMS, NUM_ORBITS)) # orbit observables for each simulation
day_ratios = np.empty((NUM_SIMS, NUM_ORBITS))
day_changes = np.empty((NUM_SIMS, NUM_ORBITS))
params_latitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS)) # residual position fit parameters for each simulation
params_longitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS))
params_altitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS))
param_coefs = (
    np.empty([NUM_ORBITS, NUM_PARAMS, 3]),
    np.empty([NUM_ORBITS, NUM_PARAMS, 3]),
    np.empty([NUM_ORBITS, NUM_PARAMS, 3]),
) # coeficients for estimating fit parameters based on night and day length


def spline_func(x_refs):
    return lambda x, *y_refs: scipy.interpolate.interp1d(x_refs, y_refs,
        kind='cubic', fill_value='extrapolate')(x)

def spline(x, x_refs, y_refs):
    return spline_func(x_refs)(x, *y_refs)


def coords_2_vec(lat_d, lon_d, alt):
    """ convert spherical coordinates to cartesian vectors """
    lat = np.radians(lat_d)
    lon = np.radians(lon_d)
    r = 6378.1 + alt
    return np.stack((r*np.cos(lat)*np.cos(lon),
                     r*np.cos(lat)*np.sin(lon),
                     r*np.sin(lat)), axis=1)


# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# >> read latitude, longitude, altitude, day length and night length from report
#    files
for i in range(NUM_SIMS):
    print('Sample: ' + str(i) + '\n')
    # -- get lat, long, alt ----------------------------------------------------
    with open(source_dir + 'ReportFile1_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
    epoch = findjuliandates.utc_to_datetime(' '.join(lines[1].split()[0:4]))
    elapsed_secs[i,:] = [float(line.split()[4]) for line in lines[1:]]
    altitude[i,:] = [float(line.split()[5]) for line in lines[1:]]
    altitude_res[i,:] = altitude[i,:] - altitude[0,:]
    latitude[i,:] = [float(line.split()[6]) for line in lines[1:]]
    latitude_res[i,:] = latitude[i,:] - latitude[0,:]
    longitude[i,:] = [float(line.split()[7]) for line in lines[1:]]
    longitude_res[i,:] = longitude[i,:] - longitude[0,:]
    longitude_res[i,:] = longitude_res[i,:] - np.floor((longitude_res[i,:]+180)/360)*360 # fix outliers that come from the periodicity of longitude

    # -- get observables ------------------------------------------------
    with open(source_dir + 'SunriseSunset_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
    type_names = [line.split()[-3] for line in lines[3:-7]]
    start_times = [findjuliandates.utc_to_seconds(' '.join(line.split()[0:4]), epoch) for line in lines[3:-7]]
    stop_times = [findjuliandates.utc_to_seconds(' '.join(line.split()[4:8]), epoch) for line in lines[3:-7]]

    for j in reversed(range(1, len(type_names))): # correct weird double-umbra events
        if type_names[j] == type_names[j-1] and start_times[j] - stop_times[j-1] < DAY_LENGTH_THRESH.total_seconds():
            type_names.pop(j)
            stop_times.pop(j-1)
            start_times.pop(j)
    for j in reversed(range(0, len(type_names))): # and weird extra umbra events
        if type_names[j] == 'Umbra' and stop_times[j] - start_times[j] < NIGHT_LENGTH_THRESH.total_seconds():
            type_names.pop(j)
            stop_times.pop(j)
            start_times.pop(j)

    sunset_times = [st for st, tn in zip(start_times, type_names) if tn=='Umbra'] # measure sunwend times for each orbit in this simulation
    sunrise_times = [st for st, tn in zip(stop_times, type_names) if tn=='Umbra'] # NOTE: these sunwends are defined by the umbra

    assert len(sunset_times) > NUM_ORBITS, "Not enough orbits were provided."

    for j in range(NUM_ORBITS): # compute observables of each orbit in this simulation
        orbit_lengths[i,j] = sunset_times[j+1] - sunset_times[j]
        day_ratios[i,j] = (sunset_times[j+1] - sunrise_times[j])/(sunrise_times[j] - sunset_times[j])
        if j == 0:
            day_changes[i,j] = 0
        else:
            day_changes[i,j] = (sunset_times[j+1] - sunrise_times[j]) - (sunset_times[j] - sunrise_times[j-1])

    # -- get fit parameters -------------------------------------------------------
    # for each start_time to start_time period, fit curve to latitude,
    # longitude and altitude and report phase shifts
    for j in range(NUM_ORBITS): # for each sunset-to-sunset period
        inds = (elapsed_secs[i] >= sunset_times[j]) &\
               (elapsed_secs[i] < sunset_times[j+1]) # pick out the enclosed indices and times
        time = elapsed_secs[i,inds]
        # fit sine curve
        # parameters A, ω, phi, d
        ω_guess = 2*np.pi/(time[-1] - time[0])

        interp_ts = np.linspace(sunset_times[j], sunset_times[j]+orbit_lengths[0,j], NUM_PARAMS)
        # >> latitude
        params_latitude[i,j,:] = curve_fit(spline_func(interp_ts), time, latitude_res[i][inds],
                                           p0=np.zeros(NUM_PARAMS))[0]
        # >> longitude
        params_longitude[i,j,:] = curve_fit(spline_func(interp_ts), time, longitude_res[i][inds],
                                            p0=np.zeros(NUM_PARAMS))[0]
        # >> altitude
        params_altitude[i,j,:] = curve_fit(spline_func(interp_ts), time, altitude_res[i][inds],
                                           p0=np.zeros(NUM_PARAMS))[0]

        if debug and i > 0:
            lat_org, lat_exp = latitude[0,inds], latitude[i,inds]
            lat_fit = lat_org + spline(time, interp_ts, params_latitude[i,j,:])
            lon_org, lon_exp = longitude[0,inds], longitude[i,inds]
            lon_fit = lon_org + spline(time, interp_ts, params_longitude[i,j,:])
            alt_org, alt_exp = altitude[0,inds], altitude[i,inds]
            alt_fit = alt_org + spline(time, interp_ts, params_altitude[i,j,:])
            pos_org = coords_2_vec(lat_org, lon_org, alt_org)
            pos_exp = coords_2_vec(lat_exp, lon_exp, alt_exp)
            pos_fit = coords_2_vec(lat_fit, lon_fit, alt_fit)
            error = pos_exp - pos_fit
            i_worst = np.argmax(np.linalg.norm(error, axis=1))
            print("The maximum error occurs at t={}s, where the fit is {:.3f}/{:.3f} km off.".format(
                  time[i_worst], np.linalg.norm(error[i_worst,:]),
                  np.linalg.norm((pos_exp-pos_org)[i_worst,:])))
            plt.figure(0)
            plt.plot(time, lat_exp-lat_org, '-')
            plt.plot(time, lat_fit-lat_org, '-')
            plt.figure(1)
            plt.plot(time, lon_exp-lon_org, '-')
            plt.plot(time, lon_fit-lon_org, '-')
            plt.figure(2)
            plt.plot(time, alt_exp-alt_org, '-')
            plt.plot(time, alt_fit-alt_org, '-')
            plt.figure(3)
            plt.axes(projection='3d')
            plt.plot(pos_exp[:,0], pos_exp[:,1], pos_exp[:,2], marker='.')
            plt.plot(pos_fit[:,0], pos_fit[:,1], pos_fit[:,2], marker='.')
            plt.plot(pos_org[:,0], pos_org[:,1], pos_org[:,2], '--')
            plt.plot(*[[pos_fit[i_worst,k], pos_exp[i_worst,k]] for k in range(3)])
            plt.show()

# :: multiple regression :::::::::::::::::::::::::::::::::::::::::::::::::::::::

for coord in range(3): # >> loop through latitude, longitude, altitude
    param_coefs[coord][0,:,:] = 0
    for j in range(1, NUM_ORBITS): # >> loop through each orbit (we can't fit for orbit 0 because we won't have any data yet)
        for k in range(NUM_PARAMS): # loop through each fit parameter
            # >> difference in observable vectors:
            x = np.stack([
                orbit_lengths[:,j-1], day_ratios[:,j-1], day_changes[:,j-1]], axis=1)
            x = x[:-1,:] - x[0,:] # (leave out the last one for testing porpoises)
            # >> value of position difference fit parameters
            if coord == 0:
                y = params_latitude[:,j,k]
            elif coord == 1:
                y = params_longitude[:,j,k]
            elif coord == 2:
                y = params_altitude[:,j,k]
            y = y[:-1]
            model = OLS(y, x).fit()
            # print("\nCoord {}, parameter {}".format(coord, k))
            # print(model.summary())
            param_coefs[coord][j,k,:] = model._results.params

            # -- plot --------------------------------------------------------------
            if debug:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(x[:,0], x[:,1], x[:,2], c=y)
                ax.set_title('Sunrise ' + str(j))
                ax.set_xlabel('delta orbit length')
                ax.set_ylabel('delta day ratio')
                ax.set_zlabel('delta day change')
                # ax.plot(x_plot, y_plot, z_plot, '.')
                plt.show()

# :: export ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

with open(source_dir+'/forecast.dat', 'wb') as f:
    f.write(NUM_SIM_DATA.to_bytes(8, 'big')) # header
    f.write(NUM_ORBITS.to_bytes(8, 'big'))
    f.write(NUM_PARAMS.to_bytes(8, 'big'))
    for t in range(NUM_SIM_DATA): # canonical GMAT data
        f.write(struct.pack('d', elapsed_secs[0,t]))
        f.write(struct.pack('d', latitude[0,t]))
        f.write(struct.pack('d', longitude[0,t]))
        f.write(struct.pack('d', altitude[0,t]))
    for j in range(NUM_ORBITS): # expected values of observables
        f.write(struct.pack('d', orbit_lengths[0,j]))
        f.write(struct.pack('d', day_ratios[0,j]))
        f.write(struct.pack('d', day_changes[0,j]))
    for coef_set in param_coefs: # coeficients relating observable residuals to spline parameters
        for j in range(NUM_ORBITS):
            for k in range(NUM_PARAMS):
                f.write(struct.pack('d', coef_set[j,k,0]))
                f.write(struct.pack('d', coef_set[j,k,1]))
                f.write(struct.pack('d', coef_set[j,k,2]))

# :: validation :::::::::::::::::::::::::::::::::::::::::::::::::::::::

for j in range(1, NUM_ORBITS): # iterate over orbits
    inds = (elapsed_secs[-1] >= sunset_times[j]) &\
           (elapsed_secs[-1] < sunset_times[j+1]) # pick out the enclosed indices and times
    time = elapsed_secs[-1,inds]
    length_res = orbit_lengths[-1,j-1] - orbit_lengths[0,j-1]
    ratio_res = day_ratios[-1,j-1] - day_ratios[0,j-1]
    change_res = day_changes[-1,j-1] - day_changes[0,j-1]

    lat_params = \
        param_coefs[0][j,:,0]*length_res +\
        param_coefs[0][j,:,1]*ratio_res +\
        param_coefs[0][j,:,2]*change_res # estimate the fit parameters from our regression results
    lon_params = \
        param_coefs[1][j,:,0]*length_res +\
        param_coefs[1][j,:,1]*ratio_res +\
        param_coefs[1][j,:,2]*change_res
    alt_params = \
        param_coefs[2][j,:,0]*length_res +\
        param_coefs[2][j,:,1]*ratio_res +\
        param_coefs[2][j,:,2]*change_res

    interp_ts = np.linspace(sunset_times[j], sunset_times[j]+orbit_lengths[0,j], NUM_PARAMS)
    lat_org, lat_exp = latitude[0,inds], latitude[-1,inds]
    lat_fit = lat_org + spline(time, interp_ts, lat_params)
    lon_org, lon_exp = longitude[0,inds], longitude[-1,inds]
    lon_fit = lon_org + spline(time, interp_ts, lon_params)
    alt_org, alt_exp = altitude[0,inds], altitude[-1,inds]
    alt_fit = alt_org + spline(time, interp_ts, alt_params)
    pos_org = coords_2_vec(lat_org, lon_org, alt_org)
    pos_exp = coords_2_vec(lat_exp, lon_exp, alt_exp)
    pos_fit = coords_2_vec(lat_fit, lon_fit, alt_fit)
    error = pos_exp - pos_fit
    i_worst = np.argmax(np.linalg.norm(error, axis=1))
    print("The maximum error occurs at t={}s, where the fit is {:.3f}/{:.3f} km off.".format(
          time[i_worst], np.linalg.norm(error[i_worst,:]),
          np.linalg.norm((pos_exp-pos_org)[i_worst,:])))

    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, lat_exp-lat_org, label="Actual")
    plt.plot(time, lat_fit-lat_org, label="Estimated") # and plot against reality!
    plt.xlabel("Time (s)")
    plt.ylabel("Latitude residual (°)")
    plt.legend()

    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, lon_exp-lon_org, label="Actual")
    plt.plot(time, lon_fit-lon_org, label="Estimated") # and plot against reality!
    plt.xlabel("Time (s)")
    plt.ylabel("Longitude residual (°)")
    plt.legend()

    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, alt_exp-alt_org, label="Actual")
    plt.plot(time, alt_fit-alt_org, label="Estimated") # and plot against reality!
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude residual (km)")
    plt.legend()

    plt.show()
