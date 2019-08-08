# 07/2019
# This script runs many GMAT scripts with slightly different initial orbital
# state and saves the latitude, longitude and altitude at each sunrise/noon/
# midnight for each script.

# ReportFile2_event_date_samplenum.txt has elapsed_secs, julian_date, latitude,
# longitude, altitude for each event occurence.

# This script will run:
# * ThinSat_Planning_SunriseSunset.script
# * ThinSat_FindLocationGivenEclipse.script

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

NUM_SAMPLES     = 100    # >> number of gmat simulations to run for each date
NUM_LAUNCHDATES = 7      # >> nuber of potential launch dates
v_scale         = 0.5e-3 # >> determines offset from initial velocity vector in km/s
r_scale         = 2.0e-3 # >> determines offset from initial position vector in km
initial_epoch   = '01 Nov 2020 13:00:00.000'
output_dir = '../../simulations/' # >> where txt files will be saved
script_dir = './' # >> where to find original scripts

import pdb
import numpy as np
import os
import shutil
import sys
import subprocess
import findjuliandates

assert shutil.which("GMAT") is not None, "You need GMAT on your path, friend."

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

np.random.seed(0)

# >> initial conditions bsed on Jack Bacon's ThinSat_PlanningPropuulsive.script
init_v = np.array([4.504094411355064, 3.530755928387845, -5.28883890677512])
init_pos = np.array([5313.19898722968, -2912.368416712065, 2580.583006475884])

# >> generate new velocity with small random offset
velocity = init_v + np.random.normal(0, v_scale, (NUM_SAMPLES, 3))
position = init_pos + np.random.normal(0, r_scale, (NUM_SAMPLES, 3))
area = np.exp(np.random.uniform(np.log(.001), np.log(.005), NUM_SAMPLES))
line_num_epoch = 11
line_num_drag = 33
line_nums_v = [19, 20, 21]
line_nums_pos = [16, 17, 18]
line_nums_out = [160, 243, 259]

# >> run simulations for each date
for d in range(NUM_LAUNCHDATES):
    print("Day {}:".format(d))
    day = '{:02d}'.format(int(initial_epoch.split()[0]) + d)
    epoch = initial_epoch.split()
    epoch[0] = day
    epoch = ' '.join(epoch)

    # >> get sunrise sunset data (0th simulation has original init conds)
    for i in range(NUM_SAMPLES):
        with open(script_dir + 'ThinSat_simulation.script', 'r') as f:
            lines = f.readlines()
            if i != 0: # >> 0th simultation has init conds
                # >> change initial velocity and position vector
                for j in range(3):
                    lines[line_nums_v[j]] = "DefaultSC.V{} = {:f};\n".format("XYZ"[j], velocity[i,j])
                    lines[line_nums_pos[j]] = "DefaultSC.{} = {:f};\n".format("XYZ"[j], position[i,j])
                # >> change drag area
                lines[line_num_drag] = "GMAT DefaultSC.DragArea = {:.3f};\n".format(area[i])

            # >> change start time
            lines[line_num_epoch] = "GMAT DefaultSC.Epoch = '{}';\n".format(epoch)

            # >> change report file location
            lines[line_nums_out[0]] = "GMAT SunriseSunset.Filename = 'SunriseSunset_d{:02d}_{:03d}.txt';\n".format(d, i) # hard as I tried to change the directory into which these go, I'm afraid you have to get them from GMAT/R2018a/output/
            lines[line_nums_out[1]] = "GMAT ReportFile1.Filename = 'ReportFile1_d{:02d}_{:03d}.txt';\n".format(d, i)
            lines[line_nums_out[2]] = "GMAT ReportFile2.Filename = 'ReportFile2_d{:02d}_{:03d}.txt';\n".format(d, i)

        # >> run gmat simulation
        script = output_dir + 'temp.script'
        with open(script, 'w') as f:
            f.write(''.join(lines))

        print("Running simulation {}".format(i))
        subprocess.run([shutil.which('GMAT'), script, '--run', '--minimize', '--exit'])
        print("Done!")
