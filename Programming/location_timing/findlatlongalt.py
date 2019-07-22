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
from mpl_toolkits.mplot3d    import Axes3D
from statsmodels.api         import OLS
from statsmodels.stats.anova import anova_lm
# sys.path.insert(0, '/home/echickles/GMAT/R2018a/userfunctions/python')
import findjuliandates

source_dir = '../../Simulations/'
debug = False

DAY_LENGTH_THRESH = datetime.timedelta(seconds=60) # no day is this short

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

reportfiles_1 = fm.filter(os.listdir(source_dir),'ReportFile1_*.txt')
reportfiles_sunrise = fm.filter(os.listdir(source_dir),
                                'ReportFile2_sunrise_*.txt')
sundata = fm.filter(os.listdir(source_dir),'SunriseSunset_*.txt')
reportfiles_1.sort()
sundata.sort()

latitude = [] # raw position data for each simulation
longitude = []
altitude = []
latitude_res = [] # residual position data for each simulation
longitude_res = []
altitude_res = []
orbit_lengths = [] # orbit observables for each simulation
day_bonuses = []
noon_times = []
elapsed_secs = [] # time vectors for each simulation
phase_shift = [] # residual position fit parameters for each simulation
params_latitude = []
params_longitude = []
params_altitude = []

# * A = amplitude
# * ω = frequency = 2pi/T
# * phi = phase shift
# * d = vertical shift
def sine(t, A, ω, phi, d):
    """ general sinusoid function """
    return A * np.sin(ω*t + phi) + d

def sone(t, A1, a2, ω, phi, d, dd):
    """ sinusoid function plus periodic linear increase """
    return sine(t, A1, ω, phi, d) + sine(t, a2*t, 2*ω, 2*phi+np.pi/2, d) + dd*np.degrees(ω*t)

def cube(t, a, b, c, d):
    """ general cubic function """
    return a*t**3 + b*t**2 + c*t + d


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
for i in range(len(reportfiles_1)):
    print('Sample: ' + str(i) + '\n')
    # -- get lat, long, alt ----------------------------------------------------
    with open(source_dir + 'ReportFile1_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
    epoch = findjuliandates.utc_to_datetime(' '.join(lines[1].split()[0:4]))
    elapsed_secs.append(np.array([float(line.split()[4]) for line in \
                                  lines[1:]]))
    altitude.append(np.array([float(line.split()[5]) for line in \
                              lines[1:]]))
    altitude_res.append(altitude[i] - altitude[0])
    latitude.append(np.array([float(line.split()[6]) for line in \
                              lines[1:]]))
    latitude_res.append(latitude[i] - latitude[0])
    longitude.append(np.array([float(line.split()[7]) for line in \
                               lines[1:]]))
    longitude_res.append(longitude[i] - longitude[0])
    longitude_res[i] = longitude_res[i] - np.floor((longitude_res[i]+180)/360)*360 # fix outliers that come from the periodicity of longitude

    # -- get observables ------------------------------------------------
    with open(source_dir + 'SunriseSunset_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
    type_names = [line.split()[-3] for line in lines[3:-7]]
    start_times = [findjuliandates.utc_to_datetime(' '.join(line.split()[0:4])) for line in lines[3:-7]]
    stop_times = [findjuliandates.utc_to_datetime(' '.join(line.split()[4:8])) for line in lines[3:-7]]

    for j in range(len(type_names)-1, 0, -1): # correct weird double-umbra events
        if type_names[j] == type_names[j-1] and start_times[j] - stop_times[j-1] < DAY_LENGTH_THRESH:
            type_names.pop(j)
            stop_times.pop(j-1)
            start_times.pop(j)

    sunset_times = [] # measure sunwend times for each orbit in this simulation
    sunrise_times = [] # NOTE: these sunwends are defined by the umbra
    for j in range(len(type_names)):
        if type_names[j] == 'Umbra':
            sunset_times.append(start_times[j])
            sunrise_times.append(stop_times[j])
    lengths = [] # compute observables of each orbit in this simulation
    bonuses = []
    times = []
    for j in range(len(sunset_times) - 1):
        lengths.append((sunset_times[j+1] - sunset_times[j]
            ).total_seconds())
        bonuses.append(((sunset_times[j+1] - sunrise_times[j]) - (sunrise_times[j] - sunset_times[j])
            ).total_seconds())
        times.append(((sunset_times[j+1] - epoch) + (sunrise_times[j] - epoch)/2
            ).total_seconds())
    orbit_lengths.append(lengths) # and append them to the complete running list
    day_bonuses.append(bonuses)
    noon_times.append(times)

    # -- get phase shift -------------------------------------------------------
    # for each start_time to start_time period, fit sine curve to latitude,
    # longitude and altitude and report phase shifts
    params_lat_list = []
    params_lon_list = []
    params_alt_list = []
    for j in range(len(sunset_times) - 1): # for each sunset-to-sunset period
        end_time = (sunset_times[j+1] - \
                    epoch).total_seconds() # pick out the bounding times
        start_time = (sunset_times[j] - \
                    epoch).total_seconds()
        inds = np.nonzero((elapsed_secs[i] >= start_time) * \
                          (elapsed_secs[i] <= end_time))[0] # and the enclosed indices and times
        time = elapsed_secs[i][inds]
        # fit sine curve
        # parameters A, ω, phi, d
        ω_guess = 2*np.pi/(end_time-start_time)

        # >> latitude
        try:
            params_lat, pcov = curve_fit(sine, time, latitude_res[i][inds],
                                     p0=[0, ω_guess, 0, 0])
        except RuntimeError:
            print('FALURE')
            params_lat = [0, ω_guess, 0, 0]
        # >> longitude
        params_lon, pcov = curve_fit(sone, time, longitude_res[i][inds],
                                     p0=[0, 0, ω_guess, 0, 0, 0])
        # >> altitude
        params_alt, pcov = curve_fit(cube, time, altitude_res[i][inds],
                                     p0=[0, 0, 0, 0])

        if debug and i > 0:
            latr_exp, latr_fit = latitude_res[i][inds], sine(time, *params_lat)
            lonr_exp, lonr_fit = longitude_res[i][inds], sone(time, *params_lon)
            altr_exp, altr_fit = altitude_res[i][inds], cube(time, *params_alt)
            pos_org = coords_2_vec(latitude[0][inds],          longitude[0][inds],          altitude[0][inds]         )
            pos_exp = coords_2_vec(latitude[0][inds]+latr_exp, longitude[0][inds]+lonr_exp, altitude[0][inds]+altr_exp)
            pos_fit = coords_2_vec(latitude[0][inds]+latr_fit, longitude[0][inds]+lonr_fit, altitude[0][inds]+altr_fit)
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
        
        # report parameters
        params_lat_list.append(params_lat)
        params_lon_list.append(params_lon)
        params_alt_list.append(params_alt)
    params_latitude.append(params_lat_list)
    params_longitude.append(params_lon_list)
    params_altitude.append(params_alt_list)

# :: multiple regression :::::::::::::::::::::::::::::::::::::::::::::::::::::::
param_coefs = [
    np.empty([np.shape(orbit_lengths)[1], len(params_latitude[0][0]), 4]),
    np.empty([np.shape(orbit_lengths)[1], len(params_longitude[0][0]), 4]),
    np.empty([np.shape(orbit_lengths)[1], len(params_altitude[0][0]), 4]),
] # coeficients for estimating fit parameters based on night and day length

for j in range(np.shape(orbit_lengths)[1]): # >> loop through each orbit
    for coord in range(3): # >> loop through latitude, longitude, altitude
        if coord == 0:
            param_values = np.array(params_latitude)
        elif coord == 1:
            param_values = np.array(params_longitude)
        elif coord == 2:
            param_values = np.array(params_altitude)
        for k in range(param_values.shape[2]): # loop through each fit parameter
            # >> difference in observable vectors:
            x = np.stack([
                [lengths[j] for lengths in orbit_lengths],
                [bonuses[j] for bonuses in day_bonuses],
                [times[j] for times in noon_times]], axis=1)
            x = x[1:,:] - x[0,:]
            # >> value of position difference fit parameters
            y = param_values[:,j,k]
            y = y[1:] - y[0]
            model = OLS(y, x).fit()
            # print(model.summary())
            param_coefs[coord][j,k,0] = np.mean(y)
            param_coefs[coord][j,k,1:] = model._results.params

            # -- plot --------------------------------------------------------------
            if j == 0 and k == 0:
                debug = True
            if debug:
                fig = plt.figure()
                ax = fig.add_subplot(111, projection='3d')
                ax.scatter(x[:,0], x[:,1], x[:,2], c=y)
                # x_plot=np.linspace(min(x), max(x), 50)
                # y_plot=np.linspace(min(y), max(y), 50)
                # X, Y = np.meshgrid(x_plot, y_plot)
                # Z = model._results.params[0] + model._results.params[1]*X +\
                #     model._results.params[2]*Y
                # surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.coolwarm,
                #                        rstride=1, cstride=1)
                ax.set_title('Sunrise ' + str(j))
                ax.set_xlabel('delta orbit length')
                ax.set_ylabel('delta day bonus')
                ax.set_zlabel('delta orbit time')
                # ax.plot(x_plot, y_plot, z_plot, '.')
            
            if debug:
                # -- plot lat, long, alt -------------------------------------------
                # sim = 10
                # plt.figure()
                # sunrise_times = np.array(sunrise_times)
                # start_time = np.mean(sunrise_times[:,j])
                # end_time = np.mean(sunrise_times[:,j+1])
                # inds = np.nonzero((elapsed_secs[j] > start_time) * \
                #               (elapsed_secs[j] < end_time))
                # time = elapsed_secs[j][inds]
                
                # # >> delta day length and delta night length
                # day_length = 3234.14 - day_lengths[sim][j] # day_lengths[0][0]
                # night_length = 2109.53 - night_lengths[sim][j] # night_lengths[0][0]
                
                # params = param_coefs[coord][j,:,0] + param_coefs[coord][j,:,1]*day_length + \
                #     param_coefs[coord][j,:,2]*night_length
                # if coord == 0:
                #     plt.plot(time, sine(time, *params), '-',
                #              label = 'Calculated latitude residual')
                # elif coord == 1:
                #     plt.plot(time, sone(time, *params), '-',
                #              label = 'Calculated longitude residual')
                # elif coord == 2:
                #     plt.plot(time, cube(time, *params), '-',
                #              label = 'Calculated altitude residual')
                
                # # -- plotting actual residual -------------------------------------
                # if coord == 0:
                #     plt.plot(time, latitude_res[sim,inds], '-',
                #              label = 'Actual latitude residual')
                # elif coord == 1:
                #     plt.plot(time, longitude_res[sim,inds], '-',
                #              label = 'Actual longitude residual')
                # elif coord == 2:
                #     plt.plot(time, altitude_res[sim,inds], '-',
                #              label = 'Actual altitude residual')
                # plt.legend()
                debug = False
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
