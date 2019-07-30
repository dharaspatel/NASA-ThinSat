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
import scipy.interpolate as spinterp
from mpl_toolkits.mplot3d    import Axes3D
from statsmodels.api         import OLS
from statsmodels.stats.anova import anova_lm
import struct
# sys.path.insert(0, '/home/echickles/GMAT/R2018a/userfunctions/python')
import findjuliandates

np.random.seed(0)


source_dir = '../../Simulations/'
debug = False

DAY_LENGTH_THRESH = datetime.timedelta(seconds=60) # no day is this short
NIGHT_LENGTH_THRESH = datetime.timedelta(seconds=60) # no night is this short

NUM_SIMS = 101 # number of simulated mission variations
NUM_ORBITS = 80 # number of orbits to fit per simulation
NUM_SIM_DATA = 14400 # number of data in each simulation
NUM_PARAMS = 9 # the number of parameters to use to fit each orbit function
NUM_MEMORIES = 9 # the number of pairs of sunwend times to remember and incorporate

MEAN_CLOCK_DRIFT = 30
SUNWEND_ERROR = 1 # the number of seconds after sunrise or before sunset it detects a sunwend

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

latitude = np.empty((NUM_SIMS, NUM_SIM_DATA)) # raw position data for each simulation
longitude = np.empty((NUM_SIMS, NUM_SIM_DATA))
altitude = np.empty((NUM_SIMS, NUM_SIM_DATA))
latitude_res = np.empty((NUM_SIMS, NUM_SIM_DATA)) # residual position data for each simulation
longitude_res = np.empty((NUM_SIMS, NUM_SIM_DATA))
altitude_res = np.empty((NUM_SIMS, NUM_SIM_DATA))
elapsed_secs = np.empty((NUM_SIMS, NUM_SIM_DATA)) # time vectors for each simulation

sunset_times = np.empty((NUM_SIMS, NUM_ORBITS)) # observable sunwends
sunrise_times = np.empty((NUM_SIMS, NUM_ORBITS))

params_latitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS)) # residual position fit parameters for each simulation
params_longitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS))
params_altitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS))
time_drifts = np.random.normal(loc=0, scale=20, size=NUM_SIMS) # the amount the clock is off, in seconds

param_coefs = (
    np.empty((NUM_ORBITS, NUM_PARAMS, 2*NUM_MEMORIES)),
    np.empty((NUM_ORBITS, NUM_PARAMS, 2*NUM_MEMORIES)),
    np.empty((NUM_ORBITS, NUM_PARAMS, 2*NUM_MEMORIES)),
    np.empty((NUM_ORBITS, 1, 2*NUM_MEMORIES)),
) # coeficients for estimating fit parameters based on night and day length


def spline_func(x_refs):
    return lambda x, *y_refs: spinterp.interp1d(x_refs, y_refs,
        kind='cubic', fill_value='extrapolate', assume_sorted=True)(x)

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

def smoothen(x):
    for i in range(1, len(x)):
        while x[i] - x[i-1] > 180:
            x[i:] -= 360
        while x[i] - x[i-1] < -180:
            x[i:] += 360
    return x


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
    longitude[i,:] = smoothen(longitude[i,:])
    longitude_res[i,:] = longitude[i,:] - longitude[0,:]

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

    sunset_times[i,:] = [st for st, tn in zip(start_times, type_names) if tn=='Umbra'][:NUM_ORBITS] # measure sunwend times for each orbit in this simulation
    sunrise_times[i,:] = [st for st, tn in zip(stop_times, type_names) if tn=='Umbra'][:NUM_ORBITS] # NOTE: these sunwends are defined by the umbra

    # -- get fit parameters -------------------------------------------------------
    # for each start_time to start_time period, fit curve to latitude,
    # longitude and altitude and report phase shifts
    for j in range(1, NUM_ORBITS): # for each sunset-to-sunset period (the zeroth one isn't complete, so ignore it)
        inds = (elapsed_secs[i,:] >= sunrise_times[0,j-1]) &\
               (elapsed_secs[i,:] < sunrise_times[0,j]) # pick out the enclosed indices and times
        time = elapsed_secs[i,inds]

        # fit spline curve
        interp_ts = np.linspace(sunrise_times[0,j-1], sunrise_times[0,j], NUM_PARAMS)
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
            print("The maximum fit error occurs at t={}s, where the fit is {:.3f}/{:.3f} km off.".format(
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

for coord in range(4): # >> loop through latitude, longitude, altitude, and time
    for j in range(1, NUM_ORBITS): # >> loop through each orbit (we can't fit for orbit 0 because we won't have enough data yet)
        # >> difference in observations
        x = np.empty((NUM_SIMS, 2*NUM_MEMORIES))
        for l in range(0, NUM_MEMORIES):
            j_prime = j - NUM_MEMORIES + l
            if j_prime >= 0:
                x[:,2*l+0] = sunset_times[:,j_prime] - sunset_times[0,j_prime] + \
                    np.random.uniform(0,SUNWEND_ERROR, NUM_SIMS) + time_drifts # stack up all recalled sunwend times
                x[:,2*l+1] = sunrise_times[:,j_prime] - sunrise_times[0,j_prime] - \
                    np.random.uniform(0,SUNWEND_ERROR, NUM_SIMS) + time_drifts # apply the time drifts
            else:
                x[:,2*l:2*l+2] = 0
        x = x[:-1,:] # (leave out the last one for testing porpoises)

        for k in range(NUM_PARAMS if coord < 3 else 1): # loop through each fit parameter (recall that time only needs one fit parameter: the time)
            # >> value of position difference fit parameters
            if coord == 0:
                y = params_latitude[:,j,k]
            elif coord == 1:
                y = params_longitude[:,j,k]
            elif coord == 2:
                y = params_altitude[:,j,k]
            elif coord == 3:
                y = time_drifts
            y = y[:-1] # (leave out the last one for testing porpoises)

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
                ax.set_xlabel('Sunset residual j-3')
                ax.set_ylabel('Sunrise residual j-3')
                ax.set_zlabel('Sunset residual j-2')
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
        f.write(struct.pack('d', sunset_times[0,j]))
        f.write(struct.pack('d', sunrise_times[0,j]))
    for coef_set in param_coefs: # coeficients relating observable residuals to spline parameters
        for j in range(NUM_ORBITS):
            for k in range(coef_set.shape[1]):
                for l in range(2*NUM_MEMORIES):
                    f.write(struct.pack('d', coef_set[j,k,l]))

# :: validation :::::::::::::::::::::::::::::::::::::::::::::::::::::::

def guess_position(sunsets, sunrises, coefficients, sunset_0, sunrise_0, latitude_0, longitude_0, altitude_0, time_0):
    """ sunsets:      the measured sunset times up until now
        sunrises:     the measured sunrise times up until now (the current time is shortly after the last one)
        coefficients: the precomputed parameter coefficients
        sunset_0:     the precomputed expected sunset times
        sunrise_0:    the precomputed expected sunrise times
        latitude_0:   the precomputed expected latitudes
        longitude_0:  the precomputed expected longitudes
        altitude_0:   the precomputed expected altitudes
        time_0:       the times that go with the precomputed coordinates
        return:       a function of time for lat, lon, alt, and the drift
    """
    orb = len(sunsets) # the orbit number
    lat_params = np.zeros(NUM_PARAMS)
    lon_params = np.zeros(NUM_PARAMS)
    alt_params = np.zeros(NUM_PARAMS)
    drift_estimate = 0
    for l in range(0, NUM_MEMORIES):
        j = orb - NUM_MEMORIES + l
        if j >= 0:
            lat_params += coefficients[0][orb,:,2*l]   * (sunsets[j]-sunset_0[j])
            lat_params += coefficients[0][orb,:,2*l+1] * (sunrises[j]-sunrise_0[j])
            lon_params += coefficients[1][orb,:,2*l]   * (sunsets[j]-sunset_0[j])
            lon_params += coefficients[1][orb,:,2*l+1] * (sunrises[j]-sunrise_0[j])
            alt_params += coefficients[2][orb,:,2*l]   * (sunsets[j]-sunset_0[j])
            alt_params += coefficients[2][orb,:,2*l+1] * (sunrises[j]-sunrise_0[j])
            drift_estimate += coefficients[3][orb,0,2*l]   * (sunsets[j]-sunset_0[j])
            drift_estimate += coefficients[3][orb,0,2*l+1] * (sunrises[j]-sunrise_0[j])
    t_interp = np.linspace(sunrise_0[orb-1], sunrise_0[orb], NUM_PARAMS)
    def func(t):
        lat = spinterp.interp1d(time_0, latitude_0)(t-drift_estimate) + spline(t-drift_estimate, t_interp, lat_params)
        lon = spinterp.interp1d(time_0, longitude_0)(t-drift_estimate) + spline(t-drift_estimate, t_interp, lon_params)
        alt = spinterp.interp1d(time_0, altitude_0)(t-drift_estimate) + spline(t-drift_estimate, t_interp, alt_params)
        return lat, lon, alt
    return drift_estimate, func

drift = 30
measured_sunsets = sunset_times[-1,:] + (1-np.random.rand(NUM_ORBITS)**2)*SUNWEND_ERROR + drift # an overestimate of the error
measured_sunrises = sunrise_times[-1,:] + (1-np.random.rand(NUM_ORBITS)**2)*SUNWEND_ERROR + drift

for j in range(1, NUM_ORBITS): # iterate over orbits
    inds = (elapsed_secs[-1] >= sunrise_times[-1,j-1]) &\
           (elapsed_secs[-1] < sunrise_times[-1,j]) # pick out the enclosed indices and times
    time = elapsed_secs[-1,inds]

    lat_org, lat_exp = latitude[0,inds], latitude[-1,inds]
    lon_org, lon_exp = longitude[0,inds], longitude[-1,inds]
    alt_org, alt_exp = altitude[0,inds], altitude[-1,inds]
    drift_estimate, position = guess_position(
        measured_sunsets[:j], measured_sunrises[:j], param_coefs,
        sunset_times[0,:], sunrise_times[0,:],
        latitude[0,:], longitude[0,:], altitude[0,:], elapsed_secs[0,:])
    lat_fit, lon_fit, alt_fit = position(time+drift)
    print("I gave it a drift of {:.1f}s, and it deduced a drift of {:.1f}s".format(drift, drift_estimate))
    pos_org = coords_2_vec(lat_org, lon_org, alt_org)
    pos_exp = coords_2_vec(lat_exp, lon_exp, alt_exp)
    pos_fit = coords_2_vec(lat_fit, lon_fit, alt_fit)
    error = pos_exp - pos_fit
    i_worst = np.argmax(np.linalg.norm(error, axis=1))
    print("The maximum error occurs at t={:.0f}s, where the fit is {:.3f}/{:.3f} km off.".format(
          time[i_worst], np.linalg.norm(error[i_worst,:]),
          np.linalg.norm((pos_exp-pos_org)[i_worst,:])))

    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, smoothen(lat_exp-lat_org), label="Actual")
    plt.plot(time, smoothen(lat_fit-lat_org), label="Estimated") # and plot against reality!
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
