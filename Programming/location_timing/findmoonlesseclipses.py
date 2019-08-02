# 07-2019
# One requirement for the pyrolysis experiment is:
# 'If there are conditions of moonless eclipse out of view of the sun's
# terminator, then this portion of the eclipse shall be the region for release.'

# This script uses moonephemeris.npy from moonephemeris.py and loadkernel.txt
# This program requires the python interface for SPICE  kernels
# >> https://github.com/AndrewAnnex/SpiceyPy

# The space that is occluded by the Earth from the satellite is represented by a
# rotated cone. The inverse of this rotation matrix is used to rotate the moon's
# position so that we can use the simple parametric equations of a cone to 
# determine if the moon is within the cone.

# Test sat pos: [-3069.960783793071, 3964.754754760618, -4319.986717816221]

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import numpy as np
import matplotlib.pyplot as plt
from   mpl_toolkits.mplot3d import Axes3D
import pdb
import spiceypy as spice

def R_2vect(vector_orig, vector_fin):
    '''Modified from https://github.com/Wallacoloo/printipi/blob/master/util/rotation_matrix.py
    Explanation of math: https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle'''
    
    vector_orig = vector_orig / np.linalg.norm(vector_orig)
    vector_fin = vector_fin / np.linalg.norm(vector_fin)

    # The rotation axis (normalised).
    axis = np.cross(vector_orig, vector_fin)
    axis_len = np.linalg.norm(axis)
    if axis_len != 0.0:
        axis = axis / axis_len

    # Alias the axis coordinates.
    x = axis[0]
    y = axis[1]
    z = axis[2]

    # The rotation angle.
    angle = np.arccos(np.dot(vector_orig, vector_fin))

    # Trig functions (only need to do this maths once!).
    ca = np.cos(angle)
    sa = np.sin(angle)

    # Calculate the rotation matrix elements.
    R = np.zeros((3,3))
    R[0,0] = 1.0 + (1.0 - ca)*(x**2 - 1.0)
    R[0,1] = -z*sa + (1.0 - ca)*x*y
    R[0,2] = y*sa + (1.0 - ca)*x*z
    R[1,0] = z*sa+(1.0 - ca)*x*y
    R[1,1] = 1.0 + (1.0 - ca)*(y**2 - 1.0)
    R[1,2] = -x*sa+(1.0 - ca)*y*z
    R[2,0] = -y*sa+(1.0 - ca)*x*z
    R[2,1] = x*sa+(1.0 - ca)*y*z
    R[2,2] = 1.0 + (1.0 - ca)*(z**2 - 1.0)
    
    return(R)

def getmoonless(sat_pos_array, time_array, threshold = 0.9, debug = False):
    '''
    ex. getmoonless([[-3069.960783793071, 3964.754754760618, -4319.986717816221]], 
        ['Nov 2, 2020'], debug = False) 

    Threshold determines how moonless eclipse needs to be to let  moonless = True.
    Threshold of 0.9 means satellite can move (1-threshold)*rad = ~465 km (~1min)
    and moon must still be out of sight for moonless = True.
    '''
    # >> get moon ephemeris
    with open('moonephemeris.txt', 'r') as f:
        lines = f.readlines()
        times_moon = [float(line.split(',')[0]) for line in lines]
        moonX = [float(line.split(',')[1]) for line in lines]
        moonY = [float(line.split(',')[2]) for line in lines]
        moonZ = [float(line.split()[0].split(',')[3]) for line in lines]

    moonless_times = []
    moon_pos_rotated = []
    inds = []
    moonless_bool = []
    
    for i in range(len(sat_pos_array)):
        sat_pos = np.array(sat_pos_array[i])
        # sat_pos = np.array([satX[i], satY[i], satZ[i]])
        spice.furnsh('./loadkernel.txt')
        time = spice.str2et(time_array[i])
        ind = np.argmin(np.abs(np.array(times_moon) - time))
        moon_pos = np.array([moonX[ind], moonY[ind], moonZ[ind]])
        # moon_pos = sat_pos_array
        # moon_pos = np.array([moonX[i], moonY[i], moonZ[i]])

        # -- calculate rotation matrix R -------------------------------------------
        R = R_2vect(np.array([0., 0., np.linalg.norm(sat_pos)]), -sat_pos)
        R_inv = np.linalg.inv(R)

        # -- determine if moon is in cone ------------------------------------------
        # >> rotate moon position vector : v_rotated = Rv
        moon_pos_rot = np.resize(np.matmul(R_inv, np.array([[moon_pos[0]], [moon_pos[1]],
                                                        [moon_pos[2]]])), (3))
        moon_pos_rotated.append(moon_pos_rot)

        # radius of circle=u/a at height z=u+sat_pos_z
        r_earth = 6371. # km
        a = (np.linalg.norm(sat_pos) - sat_pos[2]) / r_earth 
        z = moon_pos_rot[2] - sat_pos[2]
        u = z - sat_pos[2] # >> find u
        rad = np.abs(u/a) # >> find radius of circle given u
        pdb.set_trace()
        # >> test if moon is in cone (center of circle at x=0, y=0)
        dist = (moon_pos_rot[0]**2 + moon_pos_rot[1]**2)**0.5
        if dist <= threshold * rad and \
           ((moon_pos_rot[2] >= 0. and sat_pos[2] <= 0.) or \
            (moon_pos_rot[2] <= 0. and sat_pos[2] >= 0.)):
            moonless_bool.append(True)
            moonless_times.append(elapsed_secs[i])
            inds.append(i)

            # # >> debug on first moonless eclipse
            # if len(inds) == 1: debug = True
        else: moonless_bool.append(False)
        # -- plotting --------------------------------------------------------------
        # if i == 0: debug = True
        if debug:
            # >> cone parameters
            # >> radius of circle U/a = r_earth when z = mag(sat_pos) = u + sat_pos_z
            h = 240000.
            r_earth = 6371. # km
            a = (np.linalg.norm(sat_pos) - sat_pos[2]) / r_earth 
            angle = np.linspace(0, 2 * np.pi, 32)
            u = np.linspace(0, h, 32)
            theta, U = np.meshgrid(angle, u)

            # >> inverse rotate moon
            X = U * np.cos(theta) / a + sat_pos[0]
            Y = U * np.sin(theta) / a + sat_pos[1]
            if z < 0:
                Z = -(U + sat_pos[2])
            else:
                Z = U + sat_pos[2]
            fig = plt.figure()
            ax = fig.gca(projection = '3d')
            # ax.set_title('Rotated moon position, non-rotated cone: Orbit ' + str(event_num[i]))
            ax.plot_surface(X, Y, Z, rstride =1, cstride = 1)
            ax.plot([sat_pos[0]], [sat_pos[1]], [sat_pos[2]], '.', label='satellite')
            ax.plot([sat_pos[0]], [sat_pos[1]], [0.], '.', label='earth') # >> rotated earth 
            moon_pos = np.resize(np.matmul(R_inv, np.array([[moonX[i]], [moonY[i]],
                                 [moonZ[i]]])), (3))
            ax.plot([moon_pos[0]], [moon_pos[1]], [moon_pos[2]], '.', label = 'moon')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.legend(loc = 6)
            for tick in ax.xaxis.get_major_ticks():
                tick.label.set_fontsize(8) 
            for tick in ax.yaxis.get_major_ticks():
                tick.label.set_fontsize(8) 
            for tick in ax.zaxis.get_major_ticks():
                tick.label.set_fontsize(8) 
            ax.view_init(210, azim = 60)
            # plt.savefig('Cone1.png', dpi = 300)

            # >> rotate cone
            X_rotated = np.zeros(np.shape(X))
            Y_rotated = np.zeros(np.shape(X))
            Z_rotated = np.zeros(np.shape(X))
            for j in range(np.shape(X)[0]):
                for k in range(np.shape(Y)[0]):
                    vect = np.resize(np.array([X[j][k], Y[j][k], Z[j][k]]) - sat_pos, (3,1))
                    vect_rotated = np.matmul(R, vect) # (3x3)(3x1) = (3x1)
                    X_rotated[j][k], Y_rotated[j][k], Z_rotated[j][k] = \
                    np.resize(vect_rotated, (3)) + sat_pos
            fig1 = plt.figure()
            ax1 = fig1.gca(projection = '3d')
            # ax1.set_title('Rotated cone, non-rotated moon: Orbit ' + str(event_num[i]))
            ax1.plot_surface(X_rotated, Y_rotated, Z_rotated)
            ax1.plot([sat_pos[0]], [sat_pos[1]], [sat_pos[2]], '.', label='satellite')
            ax1.plot([0.], [0.], [0.], '.', label='earth')
            ax1.plot([moonX[i]], [moonY[i]], [moonZ[i]], '.', label='moon')
            ax1.set_xlabel('X')
            ax1.set_ylabel('Y')
            ax1.set_zlabel('Z')
            ax1.legend()
            plt.show()

    if len(moonless_bool) == 1:
        return moonless_bool[0]
    else:
        return moonless_bool

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


# This script uses the txt file 'ReportFile3' from 
# ThinSat_FindMoonGivenEclipse.script to determine if the moon is occluded 
# by the Earth sometime during the satellite's orbital eclipse.

# # Columns: I elapsed_secs satX satY satZ moonX moonY moonZ sunX sunY sunZ
# with open('/home/echickles/Documents/ReportFile3.txt', 'r') as f:
#     lines = f.readlines()
#     event_num    = [int(line.split()[0]) for line in lines]
#     elapsed_secs = [float(line.split()[1]) for line in lines]
#     satX  = [float(line.split()[2]) for line in lines]
#     satY  = [float(line.split()[3]) for line in lines]
#     satZ  = [float(line.split()[4]) for line in lines]
#     moonX = [float(line.split()[5]) for line in lines]
#     moonY = [float(line.split()[6]) for line in lines]
#     moonZ = [float(line.split()[7]) for line in lines]
