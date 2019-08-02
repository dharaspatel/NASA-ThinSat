# script to get moon ephemeris over three months (position every minute)

# This program requires the python interface for SPICE  kernels
# >> https://github.com/AndrewAnnex/SpiceyPy
# Tutorial on SPICE kernels:
# >> https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/Tutorials/pdf/individual_docs/18_spk.pdf

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import spiceypy as spice

# >> step size
step_size = 60

show_fig = False

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

spice.furnsh('./loadkernel.txt')
utc = ['Nov 1, 2020', 'Feb 1, 2021']
etOne = spice.str2et(utc[0]) # >> converts epoch to seconds past J2000 epoch
etTwo = spice.str2et(utc[1])
step = int((etTwo - etOne)/step_size)
print("ET One: {}, ET Two: {}".format(etOne, etTwo))
times = [x*(etTwo-etOne)/step + etOne for x in range(step)]
print(times[0:3])

# >> spkpos arguments: target body name, epoch,
#    reference frame of output pos vect, aberration correction flag,
#    observing body name
positions, lightTimes = spice.spkpos('MOON', times, 'J2000', 'NONE', 'EARTH')
print("Positions: ")
print(positions[0])

# >> save as csv file
np.save('./moonephemeris.npy', positions)

# >> plot moons position
positions = np.asarray(positions).T
fig = plt.figure(figsize=(9, 9))
ax  = fig.add_subplot(111, projection='3d')
if show_fig:
    ax.plot(positions[0], positions[1], positions[2])
    plt.show()
