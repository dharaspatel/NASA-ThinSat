# script to get moon ephemeris

# first get python interface for spice kernel
# >> https://github.com/AndrewAnnex/SpiceyPy
# tutorial:
# >> https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/Tutorials/pdf/individual_docs/18_spk.pdf

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import spiceypy as spice

# >> retrieving a state vector
# f = '/home/echickles/GMAT/R2018a/data/planetary_ephem/spk/DE424AllPlanets.bsp'
spice.furnsh('./loadkernel.txt')
# print(spice.str2et('Jun 20, 2004'))
step = 4000
utc = ['Nov 1, 2020', 'Feb 1, 2021']
etOne = spice.str2et(utc[0])
etTwo = spice.str2et(utc[1])
print("ET One: {}, ET Two: {}".format(etOne, etTwo))
times = [x*(etTwo-etOne)/step + etOne for x in range(step)]
print(times[0:3])

# >> target body name, epoch, reference frame of output pos vect, aberration correction flag
#    observing body name
positions, lightTimes = spice.spkpos('MOON', times, 'J2000', 'NONE', 'EARTH')
print("Positions: ")
print(positions[0])

positions = np.asarray(positions).T
fig = plt.figure(figsize=(9, 9))
ax  = fig.add_subplot(111, projection='3d')
ax.plot(positions[0], positions[1], positions[2])
plt.show()
