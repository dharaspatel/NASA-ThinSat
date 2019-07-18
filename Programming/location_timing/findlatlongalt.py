# This script will use observed day and night length to update the forecasted
# latitude, longitude and altitude by performing a multiple regression on
# CHANGE in day length, night length and time of sunrise to the CHANGE in phase
# shift of latitude, longitude and altitude.

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
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
# sys.path.insert(0, '/home/echickles/GMAT/R2018a/userfunctions/python')
import findjuliandates

source_dir = '../../Simulations/'
debug = False

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

reportfiles_1 = fm.filter(os.listdir(source_dir),'ReportFile1_*.txt')
reportfiles_midnight = fm.filter(os.listdir(source_dir),
                                 'ReportFile2_midnight_*.txt')
reportfiles_noon = fm.filter(os.listdir(source_dir),'ReportFile2_noon_*.txt')
reportfiles_sunrise = fm.filter(os.listdir(source_dir),
                                'ReportFile2_sunrise_*.txt')
sundata = fm.filter(os.listdir(source_dir),'SunriseSunset_*.txt')
reportfiles_1.sort()
reportfiles_midnight.sort()
reportfiles_noon.sort()
sundata.sort()

latitude = []
longitude = []
altitude = []
night_times = []
day_times = []
elapsed_secs = []
phase_shift = []
popt_latitude = []
popt_longitude = []
popt_altitude = []
sunrise_times = []
sunset_times = []
sunrise_lat = []
sunrise_long = []
sunrise_alt = []

# * A = amplitude
# * w = frequency = 2pi/T
# * phi = phase shift
# * d = vertical shift
def sine(t, A, w, phi, d):
    return A * (np.sin(w*(t+phi)) + d)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# >> read latitude, longitude, altitude, day length and night length from report
#    files
for i in range(len(reportfiles_1)):
    print('Sample: ' + str(i) + '\n')
    # -- get lat, long, alt ----------------------------------------------------
    with open(source_dir + 'ReportFile1_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
        epoch = ' '.join(lines[1].split()[0:4])
        elapsed_secs.append(np.array([float(line.split()[4]) for line in \
                                      lines[1:]]))
        altitude.append(np.array([float(line.split()[5]) for line in \
                                  lines[1:]]))
        latitude.append(np.array([float(line.split()[6]) for line in \
                                  lines[1:]]))
        longitude.append(np.array([float(line.split()[7]) for line in \
                                   lines[1:]]))

    # -- get day & night length ------------------------------------------------
    with open(source_dir + 'SunriseSunset_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
        type_names = [line.split()[-3] for line in lines[3:-7]]
        start_times = [' '.join(line.split()[0:4]) for line in lines[3:-7]]
        stop_times = [' '.join(line.split()[4:8]) for line in lines[3:-7]]
        durations = [float(line.split()[8]) for line in lines[3:-7]]
    start_times_umbra = []
    stop_times_umbra = []
    night = []
    day = []
    for j in range(len(type_names)):
        if type_names[j] == 'Umbra':
            night.append(durations[j]) 
            start_times_umbra.append(start_times[j])
            stop_times_umbra.append(stop_times[j])
    for j in range(len(start_times_umbra) - 1):
        day.append((findjuliandates.utc_to_datetime(start_times_umbra[j+1]) -\
                    findjuliandates.utc_to_datetime(stop_times_umbra[j])).total_seconds())
    night_times.append(night)
    day_times.append(day)

    # -- get phase shift -------------------------------------------------------
    # for each start_time to start_time period, fit sine curve to latitude,
    # longitude and altitude and report phase shifts
    epoch = findjuliandates.utc_to_datetime(epoch)
    popt_lat_list = []
    popt_lon_list = []
    popt_alt_list = []
    for j in range(len(start_times_umbra) - 1):
        end_time = (findjuliandates.utc_to_datetime(start_times_umbra[j+1]) - \
                    epoch).total_seconds()
        start_time = (findjuliandates.utc_to_datetime(start_times_umbra[j]) - \
                    epoch).total_seconds()
        inds = np.nonzero((elapsed_secs[i] > start_time) * \
                          (elapsed_secs[i] < end_time))
        time = elapsed_secs[i][inds]
        # fit sine curve
        # parameters A, w, phi, d
        
        # >> latitude
        popt_lat, pcov = curve_fit(sine, time, latitude[i][inds],
                                   p0 = [50, 2*np.pi/(end_time-start_time),0,0])
        # >> longitude
        try:
            popt_lon, pcov = curve_fit(sine, time, longitude[i][inds],
                                       p0 = [150, 2*np.pi/(end_time-start_time),
                                             0,0])
        except:
            inds1 = np.arange(inds[0][0]-20, inds[0][-1]+20)
            xdata = elapsed_secs[i][inds1]
            ydata= longitude[i][inds1]
            p0 = [50, 2*np.pi/(end_time-start_time), 0, 0]
            popt_lon, pcov = curve_fit(sine, xdata, ydata, p0)
        # >> altitude    
        popt_alt, pcov = curve_fit(sine, time, altitude[i][inds],
                                   p0 = [20, 2*np.pi/(end_time-start_time),0,0])
        # if i == 20:
        #     debug = True
        if debug:
            t = np.linspace(start_time, end_time, 250)
            plt.figure(0)
            plt.plot(t, sine(t, *popt_lat), '-')
            plt.plot(time, latitude[i][inds])
            plt.figure(1)
            plt.plot(t, sine(t, *popt_lon), '-')
            plt.plot(time, longitude[i][inds])
            plt.figure(2)
            plt.plot(t, sine(t, *popt_alt), '-')
            plt.plot(time, altitude[i][inds])
        # debug = False
        
        # report parameters
        popt_lat_list.append(popt_lat)
        popt_lon_list.append(popt_lon)
        popt_alt_list.append(popt_alt)
    popt_latitude.append(popt_lat_list)
    popt_longitude.append(popt_lon_list)
    popt_altitude.append(popt_alt_list)

    # -- get sunrise time, lat, long, alt --------------------------------------
    with open(source_dir + 'ReportFile2_sunrise_' + str(i) + '.txt', 'r') as f:
        lines = f.readlines()
        epoch = ' '.join(lines[1].split()[0:4])
        sunrise_times.append(np.array([float(line.split()[0]) for line in \
                                       lines]))
        sunrise_lat.append(np.array([float(line.split()[5]) for line in lines]))
        sunrise_long.append(np.array([float(line.split()[6]) for line in \
                                      lines]))
        sunrise_alt.append(np.array([float(line.split()[7]) for line in lines]))

# :: multiple regression :::::::::::::::::::::::::::::::::::::::::::::::::::::::
param = np.zeros([np.shape(day_times)[1], 3, 3])
A = np.zeros([80, 3])
w = np.zeros([80, 3])
d = np.zeros([80, 3])

for i in range(np.shape(day_times)[1]): # >> loop through each time
    for j in range(3): # >> loop through latitude, longitude, altitude
        # >> difference in day length:
        x = [sample[i] - day_times[0][i] for sample in day_times[1:]]
        # >> difference in night length: 
        y = [sample[i] - night_times[0][i] for sample in night_times[1:]]
        # >> difference in phase shift
        if j == 0:
            z = [popt[i][2] - popt_latitude[0][i][2] for popt in \
                 popt_latitude[1:]]
        elif j == 1:
            z = [popt[i][2] - popt_longitude[0][i][2] for popt in \
                 popt_longitude[1:]]
        else:
            z = [popt[i][2] - popt_altitude[0][i][2] for popt in \
                 popt_altitude[1:]]
        data = pandas.DataFrame({'x': x, 'y': y, 'z': z})
        model = ols("z ~ x + y", data).fit()
        param[i][j] = model._results.params
        # print(model.summary())

        # -- plot --------------------------------------------------------------
        if i == 0:
            debug = True
        if debug:
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(x, y, z, '.')
            x_plot=np.linspace(min(x), max(x), 50)
            y_plot=np.linspace(min(y), max(y), 50)
            #z_plot=model._results.params[0] + model._results.params[1]*x_plot + \
            #       model._results.params[2]*y_plot
            X, Y = np.meshgrid(x_plot, y_plot)
            Z = model._results.params[0] + model._results.params[1]*X +\
                model._results.params[2]*Y
            surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.coolwarm,
                                   rstride=1, cstride=1)
            ax.set_title('Sunrise ' + str(i))
            ax.set_xlabel('X: delta day length')
            ax.set_ylabel('Y: delta night length')
            if j == 0:
                ax.set_zlabel('Z: delta phi latitude')
            elif j == 1:
                ax.set_zlabel('Z: delta phi longitude')
            else:
                ax.set_zlabel('Z: delta phi altitude')
            # ax.plot(x_plot, y_plot, z_plot, '.')

            
        # -- calculate A, w, d -------------------------------------------------
        A[i][0] = np.mean([popt[i][0] for popt in popt_latitude])
        A[i][1] = np.mean([popt[i][0] for popt in popt_longitude])
        A[i][2] = np.mean([popt[i][0] for popt in popt_altitude])
        w[i][0] = np.mean([popt[i][1] for popt in popt_latitude])
        w[i][1] = np.mean([popt[i][1] for popt in popt_longitude])
        w[i][2] = np.mean([popt[i][1] for popt in popt_altitude])
        d[i][0] = np.mean([popt[i][3] for popt in popt_latitude])
        d[i][1] = np.mean([popt[i][3] for popt in popt_longitude])
        d[i][2] = np.mean([popt[i][3] for popt in popt_altitude])
        
        if debug:
            # -- plot lat, long, alt -------------------------------------------
            plt.figure()
            sunrise_times = np.array(sunrise_times)
            start_time = np.mean(sunrise_times[:,i])
            end_time = np.mean(sunrise_times[:,i+1])
            t = np.linspace(start_time, end_time, 250)
            
            # >> delta day length and delta night length
            day_length = 3234.14 - day_times[0][i] # day_times[0][0]
            night_length = 2109.53 - night_times[0][i] # night_times[0][0]
            
            if j == 0:
                phi = param[i][0][0] + param[i][0][1]*day_length + \
                     param[i][0][2]*night_length + popt_latitude[0][i][2]
                plt.plot(t, sine(t, A[i][0], w[i][0], phi, d[i][0]), '-',
                         label = 'Calculated latitude')
            elif j == 1:
                phi = param[i][1][0] + param[i][1][1]*day_length + \
                      param[i][1][2]*night_length + popt_longitude[0][i][2]
                plt.plot(t, sine(t, A[i][1], w[i][1], phi, d[i][1]), '-',
                         label = 'Calculated longitude')
            elif j == 2:
                phi = param[i][2][0] + param[i][2][1]*day_length + \
                      param[i][2][2]*night_length + popt_altitude[0][i][2]
                plt.plot(t, sine(t, A[i][2], w[i][2], phi, d[i][2]), '-',
                         label = 'Calculated altitude')
            
            # -- plotting actual location -------------------------------------             
            inds = np.nonzero((elapsed_secs[i] > start_time) * \
                          (elapsed_secs[i] < end_time))
            time = elapsed_secs[i][inds]
            if j == 0:
                plt.plot(time, latitude[i][inds], '-',
                         label = 'Actual latitude')
            elif j == 1:
                plt.plot(time, longitude[i][inds], '-',
                         label = 'Actual longitude')
            elif j == 2:
                plt.plot(time, altitude[i][inds], '-',
                         label = 'Actual altitude')
            plt.legend()
            debug = False
plt.show()        
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            
# # plot day length against altitude
# day_1 = [time[0] for time in day_times]
# phi_alt_1 = [popt[0][2] for popt in popt_altitude]
# plt.figure(0)
# plt.plot(day_1, phi_alt_1, '.')

# # plot day length against latitude
# phi_lat_1 = [popt[0][2] for popt in popt_latitude]
# plt.figure(1)
# plt.plot(day_1, phi_lat_1, '.')

# # plot day length against longitude
# phi_long_1 = [popt[0][2] for popt in popt_longitude]
# plt.figure(2)
# plt.plot(day_1, phi_long_1, '.')

# # plot night length against altitude
# night_1 = [time[0] for time in night_times]
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
#     x[i][1] = day_times[i][0]
#     x[i][2] = night_times[i][0]
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
#     day[i] = day_times[i][0]
#     nit[i] = night_times[i][0]
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
    #     night_times.append(t)
        

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

# for i in range(len(night_times)):
#     dur.append(night_times[i][time])
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
#     t = (findjuliandates.utc_to_datetime(sunset_times[i][time]) - findjuliandates.utc_to_datetime(sunrise_times[i][time])).total_seconds()
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