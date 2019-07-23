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
noon_times = np.empty((NUM_SIMS, NUM_ORBITS))
params_latitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS)) # residual position fit parameters for each simulation
params_longitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS))
params_altitude = np.empty((NUM_SIMS, NUM_ORBITS, NUM_PARAMS))


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
        orbit_lengths[i,:] = sunset_times[j+1] - sunset_times[j]
        day_ratios[i,:] = (sunset_times[j+1] - sunrise_times[j])/(sunrise_times[j] - sunset_times[j])
        noon_times[i,:] = (sunset_times[j+1] + sunrise_times[j])/2

    # -- get phase shift -------------------------------------------------------
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
            latr_exp, latr_fit = latitude_res[i,inds], spline(time, interp_ts, params_latitude[i,j,:])
            lonr_exp, lonr_fit = longitude_res[i,inds], spline(time, interp_ts, params_longitude[i,j,:])
            altr_exp, altr_fit = altitude_res[i,inds], spline(time, interp_ts, params_altitude[i,j,:])
            pos_org = coords_2_vec(latitude[0,inds],          longitude[0,inds],          altitude[0,inds]         )
            pos_exp = coords_2_vec(latitude[0,inds]+latr_exp, longitude[0,inds]+lonr_exp, altitude[0,inds]+altr_exp)
            pos_fit = coords_2_vec(latitude[0,inds]+latr_fit, longitude[0,inds]+lonr_fit, altitude[0,inds]+altr_fit)
            error = pos_exp - pos_fit
            i_worst = np.argmax(np.linalg.norm(error, axis=1))
            print("The maximum error occurs at t={}s, where the fit is {:.3f}/{:.3f} km off.".format(
                  time[i_worst], np.linalg.norm(error[i_worst,:]),
                  np.linalg.norm((pos_exp-pos_org)[i_worst,:])))
            plt.figure(0)
            plt.plot(time, latr_fit, '-')
            plt.plot(time, latr_exp, '-')
            plt.figure(1)
            plt.plot(time, lonr_fit, '-')
            plt.plot(time, lonr_exp, '-')
            plt.figure(2)
            plt.plot(time, altr_fit, '-')
            plt.plot(time, altr_exp, '-')
            plt.figure(3)
            plt.axes(projection='3d')
            plt.plot(pos_fit[:,0], pos_fit[:,1], pos_fit[:,2], marker='.')
            plt.plot(pos_exp[:,0], pos_exp[:,1], pos_exp[:,2], marker='.')
            plt.plot(*[[pos_fit[i_worst,k], pos_exp[i_worst,k]] for k in range(3)])
            plt.show()

# :: multiple regression :::::::::::::::::::::::::::::::::::::::::::::::::::::::
param_coefs = (
    np.empty([NUM_ORBITS, NUM_PARAMS, 4]),
    np.empty([NUM_ORBITS, NUM_PARAMS, 4]),
    np.empty([NUM_ORBITS, NUM_PARAMS, 4]),
) # coeficients for estimating fit parameters based on night and day length

for j in range(NUM_ORBITS): # >> loop through each orbit
    for coord in range(3): # >> loop through latitude, longitude, altitude
        for k in range(NUM_PARAMS): # loop through each fit parameter
            # >> difference in observable vectors:
            x = np.stack([
                orbit_lengths[:,j], day_ratios[:,j], noon_times[:,j]], axis=1)
            x = x[1:-1,:] - x[0,:] # (leave out the last one for testing porpoises)
            # >> value of position difference fit parameters
            if coord == 0:
                y = params_latitude[:,j,k]
            elif coord == 1:
                y = params_longitude[:,j,k]
            elif coord == 2:
                y = params_altitude[:,j,k]
            y = y[1:-1] - y[0]
            model = OLS(y, x).fit()
            # print("\nCoord {}, parameter {}".format(coord, k))
            # print(model.summary())
            param_coefs[coord][j,k,0] = np.mean(y)
            param_coefs[coord][j,k,1:] = model._results.params

            # -- plot --------------------------------------------------------------
            if debug:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(x[:,0], x[:,1], x[:,2], c=y)
                ax.set_title('Sunrise ' + str(j))
                ax.set_xlabel('delta orbit length')
                ax.set_ylabel('delta day ratio')
                ax.set_zlabel('delta noon time')
                # ax.plot(x_plot, y_plot, z_plot, '.')
                plt.show()

# :: validation :::::::::::::::::::::::::::::::::::::::::::::::::::::::

for j in range(NUM_ORBITS): # iterate over orbits
    inds = (elapsed_secs[-1] >= sunset_times[j]) &\
           (elapsed_secs[-1] < sunset_times[j+1]) # pick out the enclosed indices and times
    time = elapsed_secs[-1,inds]
    length_res = orbit_lengths[-1,j] - orbit_lengths[0,j]
    ratio_res = day_ratios[-1,j] - day_ratios[0,j]
    noon_res = noon_times[-1,j] - noon_times[0,j]

    interp_ts = np.linspace(sunset_times[j], sunset_times[j]+orbit_lengths[0,j], NUM_PARAMS)

    lat_params = param_coefs[0][j,:,0] +\
        param_coefs[0][j,:,1]*length_res +\
        param_coefs[0][j,:,2]*ratio_res +\
        param_coefs[0][j,:,3]*noon_res # estimate the fit parameters from our regression results
    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, latitude_res[-1,inds], label="Actual")
    plt.plot(time, spline(time, interp_ts, lat_params), label="Estimated") # and plot against reality!
    plt.xlabel("Time (s)")
    plt.ylabel("Latitude residual (°)")
    plt.legend()

    lon_params = param_coefs[1][j,:,0] +\
        param_coefs[1][j,:,1]*length_res +\
        param_coefs[1][j,:,2]*ratio_res +\
        param_coefs[1][j,:,3]*noon_res # estimate the fit parameters from our regression results
    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, longitude_res[-1,inds], label="Actual")
    plt.plot(time, spline(time, interp_ts, lon_params), label="Estimated") # and plot against reality!
    plt.xlabel("Time (s)")
    plt.ylabel("Longitude residual (°)")
    plt.legend()

    alt_params = param_coefs[2][j,:,0] +\
        param_coefs[2][j,:,1]*length_res +\
        param_coefs[2][j,:,2]*ratio_res +\
        param_coefs[2][j,:,3]*noon_res # estimate the fit parameters from our regression results
    plt.figure()
    plt.title("Orbit {}".format(j))
    plt.plot(time, altitude_res[-1,inds], label="Actual")
    plt.plot(time, spline(time, interp_ts, alt_params), label="Estimated") # and plot against reality!
    plt.xlabel("Time (s)")
    plt.ylabel("Altitude residual (°)")
    plt.legend()

    plt.show()

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# # plot day length against altitude
# day_1 = [time[0] for time in day_lengths]
# phi_alt_1 = [params[0][2] for params in params_altitude]
# plt.figure(0)
# plt.plot(day_1, phi_alt_1, '.')

# # plot day length against latitude
# phi_lat_1 = [params[0][2] for params in params_latitude]
# plt.figure(1)
# plt.plot(day_1, phi_lat_1, '.')

# # plot day length against longitude
# phi_long_1 = [params[0][2] for params in params_longitude]
# plt.figure(2)
# plt.plot(day_1, phi_long_1, '.')

# # plot night length against altitude
# night_1 = [time[0] for time in night_lengths]
# plt.figure(3)
# plt.plot(night_1, phi_alt_1, '.')

# # plot night length against latitude
# plt.figure(4)
# plt.plot(night_1, phi_lat_1, '.')

# # plot night length against longitude
# plt.figure(5)
# plt.plot(night_1, phi_long_1, '.')

# save txt file (phase shift for lat, long, alt)
# col 1: time of first sunrise
# col 2: night length
# col 3: day length
# col 4: latitude at first sunrise
# col 5: longitude at first sunrise
# col 6: altitude at first sunrise
# x = np.zeros([len(reportfiles_1), 6])
# for i in range(len(reportfiles_1)):
#     x[i][0] = sunrise_times[i][0]
#     x[i][1] = day_lengths[i][0]
#     x[i][2] = night_lengths[i][0]
#     x[i][3] = sunrise_lat[i][0]
#     x[i][4] = sunrise_long[i][0]
#     x[i][5] = sunrise_alt[i][0]
# np.savetxt('samplesize50sunrise1.txt', x, delimiter = ',')
    
# have altitude, latitude, longitude for first sunrise
# have length of night, length of day
# alt = np.zeros(50)
# lat = np.zeros(50)
# lon = np.zeros(50)
# day = np.zeros(50)
# nit = np.zeros(50)
# sec = np.zeros(50)
# for i in range(len(altitude)):
#     alt[i] = altitude[i][0]
#     lat[i] = latitude[i][0]
#     lon[i] = longitude[i][0]
#     day[i] = day_lengths[i][0]
#     nit[i] = night_lengths[i][0]
#     sec[i] = elapsed_secs[i][0]
        
    # with open(source_dir + reportfiles_midnight[i], 'r') as f:
    #     lines = f.readlines()
    #     times_utc.append([line.split()[0] for line in lines])
    #     latitude.append([float(line.split()[-3]) for line in lines])
    #     longitude.append([float(line.split()[-2]) for line in lines])
    #     altitude.append([float(line.split()[-1]) for line in lines])

    # with open(source_dir + 'ReportFile1_' + str(i) + '.txt', 'r') as f:
    #     lines = f.readlines()
    # epoch = ' '.join(lines[1].split()[0:4])

    # with open(source_dir + 'SunriseSunset_' + str(i) + '.txt', 'r') as f:
    #     lines = f.readlines()
    #     type_names = [line.split()[-3] for line in lines[3:-7]]
    #     t = [float(line.split()[-1]) for line in lines[3:-7]]
    #     night_lengths.append(t)
        

# sunrise_times1, sunset_times1 = findjuliandates.getmidtimes(source_dir + "SunriseSunset_" + str(i) + '.txt', epoch, reporttimes = True)
# sunrise_times.append(sunrise_times1)
# sunset_times.append(sunset_times1)

# plot time of night with altitude
# plt.ion()
# elapsed_secs = []
# alt = []
# lat = []
# lon = []
# dur = []
# time = 10

# for i in range(len(night_lengths)):
#     dur.append(night_lengths[i][time])
#     alt.append(altitude[i][time])
#     lat.append(latitude[i][time])
#     lon.append(longitude[i][time])

# plt.figure(0)
# plt.plot(dur, alt, '.')
# plt.xlabel('Time between sunset and sunrise(s)')
# plt.ylabel('Altitude (km)')

# plt.figure(1)
# plt.plot(dur, lat, '.')

# plt.figure(2)
# plt.plot(dur, lon, '.')

# given orbital period, night time 


# for i in range(len(sunrise_times)):
#     # !! why is there a negative thing???
#     t = (sunset_times[i][time] - sunrise_times[i][time]).total_seconds()
#     if t > 0:
#         if False:
#             print(i)
#         else:
#             elapsed_secs.append(t)
#             alt.append(float(altitude[i][time]))
#             lat.append(float(latitude[i][time]))
#             lon.append(float(longitude[i][time]))
#     else:
#         print(i)
# plt.figure(0)
# plt.plot(elapsed_secs, alt, '.')

# plt.figure(1)
# plt.plot(elapsed_secs, lat, '.')

# plt.figure(2)
# plt.plot(elapsed_secs, lon, '.')
