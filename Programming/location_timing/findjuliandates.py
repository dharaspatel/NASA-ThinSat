# use GMAT's eclipse locator report to get elapsed seconds of each event

import pdb
import datetime
#import jdcal

def utc_to_datetime(time_utc):
    time_utc = time_utc.split('.')
    ms = '.' + time_utc[1]
    ms = '%6d' % (float(ms) * 10e5)
    time_utc = '.'.join(time_utc)
    fmt = '%d %b %Y %H:%M:%S.%f'
    return datetime.datetime.strptime(time_utc, fmt)

def utc_to_seconds(time_utc, epoch=datetime.datetime(1970, 1, 1)):
    return (utc_to_datetime(time_utc) - epoch).total_seconds()

def gettimes(filename, epoch):
    # offset = 2430000.0 # stupid offset because stupid gmat
    # http://gmat.sourceforge.net/docs/nightly/html/SpacecraftEpoch.html
    with open(filename, 'r') as f:
        lines = f.readlines()
        times_utc = [' '.join(line.split()[0:4]) for line in lines[3:-7]]
    times_julian = []
    elapsed_days = []
    elapsed_secs = []
    for i in range(len(times_utc)):
        dt = utc_to_datetime(times_utc[i])
        elapsed_secs.append( (dt - epoch).total_seconds() )
        
        # find fractional day
        #f = (dt - datetime.datetime(dt.year, dt.month, dt.day)).total_seconds()\
        #    /(24*60*60)
        #dt_jul = sum(jdcal.gcal2jd(dt.year, dt.month, dt.day)) + f - offset
        #times_julian.append(dt_jul)
        #elapsed_days.append(dt_jul - epoch)
        #elapsed_secs.append((dt_jul - epoch)*24*60*60)
    return elapsed_secs
        
def getmidtimes(filename, epoch, reportlen = False, reporttimes = False):
    # 17 Apr 2018 23:59:23.000
    with open(filename, 'r') as f:
        lines = f.readlines()
        type_names = [line.split()[-3] for line in lines[3:-7]]
        times_utc = [' '.join(line.split()[0:4]) for line in lines[3:-7]]
        times_julian = []
    sunrise_times = []
    sunset_times = []
    for i in range(len(type_names)):
        if type_names[i] == 'Penumbra':
            if i < len(type_names) - 2:
                if type_names[i+1] == 'Umbra': #sunset
                    sunset_times.append(times_utc[i])
            else:
                if type_names[i-2] == 'Umbra':
                    sunset_times.append(times_utc[i])
            if i < len(type_names) - 3:
                if type_names[i+2] == 'Umbra': #sunrise
                    sunrise_times.append(times_utc[i])
            else:
                if type_names[i-1] == 'Umbra':
                    sunset_times.append(times_utc[i])
    elapsed_secs = []

    # want to start from first sunset
    t_sunset = utc_to_datetime(sunset_times[0])
    t_sunrise = utc_to_datetime(sunrise_times[0])
    if t_sunset < t_sunrise:
        sunset_times = sunset_times[1:]

    for i in range(min([len(sunset_times), len(sunrise_times)])):
        t_sunset = utc_to_datetime(sunset_times[i])
        t_sunrise = utc_to_datetime(sunrise_times[i])
        dt = (t_sunset - t_sunrise) / 2
        # if dt < 0:
        elapsed_secs.append( (t_sunrise + dt - epoch).total_seconds() )
    if reportlen:
        return len(elapsed_secs)
    elif reporttimes:
        return sunrise_times, sunset_times
    else:
        return elapsed_secs

def getmidnighttimes(filename, epoch, reportlen = False, reporttimes = False):
    # 17 Apr 2018 23:59:23.000
    with open(filename, 'r') as f:
        lines = f.readlines()
        type_names = [line.split()[-3] for line in lines[3:-7]]
        start_times = [' '.join(line.split()[0:4]) for line in lines[3:-7]]
        stop_times = [' '.join(line.split()[4:8]) for line in lines[3:-7]]
    elapsed_secs = []
    for i in range(len(type_names)):
        if type_names[i] == 'Umbra':
            dt = utc_to_datetime(stop_times[i]) - utc_to_datetime(start_times[i])
            t_utc = utc_to_datetime(start_times[i]) + dt/2
            t_secs = (t_utc - epoch).total_seconds()
            elapsed_secs.append(t_secs)
    if reportlen:
        return len(elapsed_secs)
    else:
        return elapsed_secs

def getnoontimes(filename, epoch, reportlen = False, reporttimes = False):
    # 17 Apr 2018 23:59:23.000
    import datetime
    with open(filename, 'r') as f:
        lines = f.readlines()
        type_names = [line.split()[-3] for line in lines[3:-7]]
        start_times = [' '.join(line.split()[0:4]) for line in lines[3:-7]]
        stop_times = [' '.join(line.split()[4:8]) for line in lines[3:-7]]
    elapsed_secs = []
    start_times_umbra = []
    stop_times_umbra = []
    for i in range(len(type_names)):
        if type_names[i] == 'Umbra':
            start_times_umbra.append(start_times[i])
            stop_times_umbra.append(stop_times[i])
    for i in range(len(start_times_umbra) - 1):
        dt = utc_to_datetime(start_times_umbra[i+1]) - \
            utc_to_datetime(stop_times_umbra[i])
        t_utc = utc_to_datetime(stop_times_umbra[i]) + dt/2
        t_secs = (t_utc - epoch).total_seconds()
        elapsed_secs.append(t_secs)
    if reportlen:
        return len(elapsed_secs)
    else:
        return elapsed_secs
            
def getsunrisetimes(filename, epoch, reportlen = False, reporttimes = False):
    # 17 Apr 2018 23:59:23.000
    with open(filename, 'r') as f:
        lines = f.readlines()
        type_names = [line.split()[-3] for line in lines[3:-7]]
        times_utc = [' '.join(line.split()[0:4]) for line in lines[3:-7]]
    elapsed_secs = []
    for i in range(len(type_names)):
        if type_names[i] == 'Penumbra':
            if type_names[i-1] == 'Umbra' and i > 0:
                dt = utc_to_datetime(times_utc[i]) - epoch
                elapsed_secs.append(dt.total_seconds())
    if reportlen:
        return len(elapsed_secs)
    else:
        return elapsed_secs
