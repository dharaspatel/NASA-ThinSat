import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

import findjuliandates


NUM_ORBITS = 6
MIN_SIM = 23 # this would be 0 if Emma weren't so weird
MAX_SIM = 101

SOURCE_DIR = '../../Simulations/'

DAY_LENGTH_THRESH = datetime.timedelta(seconds=60) # no day is this short
NIGHT_LENGTH_THRESH = datetime.timedelta(seconds=60) # no night is this short


if __name__ == '__main__':
	num_orbits = np.empty((MAX_SIM-MIN_SIM, 1))
	night_lengths = np.empty((MAX_SIM-MIN_SIM, NUM_ORBITS))
	orbit_lengths = np.empty((MAX_SIM, NUM_ORBITS))

	for i in range(0, MAX_SIM-MIN_SIM):
		with open(SOURCE_DIR + '00/' + 'SunriseSunset_Nov30_' + str(MIN_SIM+i) + '.txt', 'r') as f:
			lines = f.readlines()
		epoch = findjuliandates.utc_to_datetime(' '.join(lines[3].split()[0:4]))
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

		set_times = [st for st, tn in zip(start_times, type_names) if tn=='Umbra'] # measure sunwend times for each orbit in this simulation
		rise_times = [st for st, tn in zip(stop_times, type_names) if tn == 'Umbra']
		for j in range(-1, -1-NUM_ORBITS, -1):
			orbit_lengths[i,j] = set_times[j] - set_times[j-1]
			night_lengths[i,j] = rise_times[j-1] - set_times[j-1] if rise_times[j-1] > set_times[j-1] else rise_times[j] - set_times[j-1]
		num_orbits[i,0] = len(set_times)

	inds = np.argsort(num_orbits[:,0]) # it bothers me that I have to do this
	num_orbits = num_orbits[inds]
	orbit_lengths = orbit_lengths[inds]
	night_lenghts = night_lengths[inds]
	day_lengths = orbit_lengths - night_lengths

	sns.set_palette(sns.cubehelix_palette(NUM_ORBITS, start=.6, rot=-.75, light=.7, reverse=True))
	for j in range(NUM_ORBITS):
		label = (NUM_ORBITS-j-2)*"ante"+"penultimate" if j < NUM_ORBITS-1 else "final"
		plt.scatter(orbit_lengths[:,j]/60, day_lengths[:,j]/60, s=5+2*j, label=label.capitalize())
	plt.xlabel("Length of orbit")
	plt.ylabel("Length of day")
	plt.legend()
	plt.show()
