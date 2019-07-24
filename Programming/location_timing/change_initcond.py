# 07/2019
# This script runs many GMAT scripts with slightly different initial orbital
# state and saves the latitude, longitude and altitude at each sunrise/noon/
# midnight for each script.

# ReportFile2_event_samplenum.txt has elapsed_secs, julian_date, latitude,
# longitude, altitude for each event occurence.

# This script will run:
# * ThinSat_Planning_SunriseSunset.script
# * ThinSat_FindLocationGivenEclipse.script

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

samples    = 2      # >> number of gmat simulations to run
scale      = 1.0e-3 # >> determines offset from initial velocity vector
output_dir = '/home/echickles/Documents/' # >> where txt files will be saved
script_dir = '/home/echickles/Documents/' # >> where to find original scripts
noon, midnight,  sunrise = False, False, True # >> events to find location

import pdb
import numpy as np
import os
import sys
sys.path.insert(0, '/home/echickles/GMAT/R2018a/userfunctions/python')
import findjuliandates

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# >> initial conditions bsed on Jack Bacon's ThinSat_PlanningPropuulsive.script
init_v = np.array([4.504094411355064, 3.530755928387845, -5.28883890677512])

# >> generate new velocity with small random offset
velocity = init_v + np.random.normal(0, scale, (samples, 3))
line_nums = [18, 19, 20]

# >> get sunrise sunset data (0th simulation has original init conds)
for i in range(samples+1):
    with open(script_dir + 'ThinSat_Planning_SunriseSunset.script', 'r') as f:
        lines = f.readlines()
        # >> change initial velocity vector
        for j in range(3):
            if i != 0: # >> 0th simultation has init conds
                new = lines[line_nums[j]].split(' ')
                new[2] = str(velocity[i-1][j]) + '\n'
                lines[line_nums[j]] = ' '.join(new)

    filename = output_dir + 'ThinSat_simulation.script'
    with open(filename, 'w') as f:
        f.write(''.join(lines))

    # >> run gmat simulation
    os.chdir("/home/echickles/GMAT/R2018a/bin")
    os.system("./GmatConsole " + filename)

    # >> move report files
    os.rename("/home/echickles/GMAT/R2018a/output/ReportFile1.txt",
              output_dir + "ReportFile1_" + \
              str(i) + '.txt')
    os.rename("/home/echickles/GMAT/R2018a/output/SunriseSunset.txt",
              output_dir + "SunriseSunset_" + \
              str(i) + '.txt')

    # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # >> get latitude and longitude and altitude for noon, midnights, sunrises

    # now only want sunrise data
    inds = np.nonzero([noon, midnight, sunrise])
    for t in inds[0]:
        if t == 0:
            noon, midnight, sunrise = True, False, False
        elif t == 1:
            noon, midnight, sunrise = False, True, False
        else:
            noon, midnight, sunrise = False, False, True

        # >> get epoch
        with open(output_dir + 'ReportFile1_' + str(i) + '.txt', 'r') as f:
            lines = f.readlines()
        epoch = ' '.join(lines[1].split()[0:4])

        if noon:
            num_data = findjuliandates.getnoontimes(output_dir+"SunriseSunset_" \
                                                    + str(i) + '.txt',
                                                    epoch, reportlen = True)
        if midnight:
            num_data = findjuliandates.getmidnighttimes(output_dir + \
                                                        "SunriseSunset_" + \
                                                        str(i) + '.txt',
                                                        epoch, reportlen = True)
        if sunrise:
            num_data = findjuliandates.getsunrisetimes(output_dir + \
                                                        "SunriseSunset_" + \
                                                        str(i) + '.txt',
                                                        epoch, reportlen = True)
            
        with open(script_dir + 'ThinSat_FindLocationGivenEclipse.script',
                  'r') as f:
            lines = f.readlines()

            # -- modifying script ----------------------------------------------
            for j in range(3):
                new = lines[line_nums[j]].split(' ')
                new[2] = str(velocity[i-1][j]) + '\n'
                lines[line_nums[j]] = ' '.join(new)
            
            # >> changing array size
            new = lines[196].split()
            new[2] = 'times[' + str(num_data) + '];\n'
            lines[196] = ' '.join(new)
            new = 'For I = 1:1:' + str(num_data - 1)  +';\n'
            lines[217] = new

            # >> changing file name
            new = lines[205].split()
            new[2] = "'" + output_dir + "SunriseSunset_" + str(i) + ".txt'\n"
            lines[205] = ' '.join(new)

            if noon:
                lines[211] = 'times = Python.findjuliandates.getnoontimes(p1, p2)\n'
            if midnight:
                lines[211] = 'times = Python.findjuliandates.getmidnighttimes(p1, p2)\n'
            if sunrise:
                lines[211] = 'times = Python.findjuliandates.getsunrisetimes(p1, p2)\n'

            # ------------------------------------------------------------------

        filename = output_dir + 'ThinSat_FindLocation_sunrise.script'
        with open(filename, 'w') as f:
            f.write(''.join(lines))

        # >> run gmat simulation
        os.chdir("/home/echickles/GMAT/R2018a/bin")
        os.system("./GmatConsole " + filename)

        #  >> move report files
        if noon:
            os.rename("/home/echickles/GMAT/R2018a/output/ReportFile2.txt",
                      output_dir + "ReportFile2_noon_" + \
                      str(i) + '.txt')
        if midnight:
            os.rename("/home/echickles/GMAT/R2018a/output/ReportFile2.txt",
                      output_dir + "ReportFile2_midnight_" + \
                      str(i) + '.txt')
        if sunrise:
            os.rename("/home/echickles/GMAT/R2018a/output/ReportFile2.txt",
                      output_dir + "ReportFile2_sunrise_" + \
                      str(i) + '.txt')
        
# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
