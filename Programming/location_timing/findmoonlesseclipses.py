# 07-2019
# One requirement for the pyrolysis experiment is:
# 'If there are conditions of moonless eclipse out of view of the sun's
# terminator, then this portion of the eclipse shall be the region for release.'
# This script uses the txt file 'ReportFile3' from 
# ThinSat_FindMoonGivenEclipse.script to determine if the moon is occluded 
# by the Earth sometime during the satellite's orbital eclipse.

# The space that is occluded by the Earth from the satellite is represented by a
# rotated cone. The inverse of this rotation matrix is used to rotate the moon's
# position so that we can use the simple parametric equations of a cone to 
# determine if the moon is within the cone.

# TO DO:
# * find optimal trigger time given other constraints (such as altitude)

# ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pdb

# Columns: I elapsed_secs satX satY satZ moonX moonY moonZ sunX sunY sunZ
with open('./ReportFile3.txt', 'r') as f:
    lines = f.readlines()
    event_num    = [int(line.split()[0]) for line in lines]
    elapsed_secs = [float(line.split()[1]) for line in lines]
    satX  = [float(line.split()[2]) for line in lines]
    satY  = [float(line.split()[3]) for line in lines]
    satZ  = [float(line.split()[4]) for line in lines]
    moonX = [float(line.split()[5]) for line in lines]
    moonY = [float(line.split()[6]) for line in lines]
    moonZ = [float(line.split()[7]) for line in lines]

moonless_times = []
orbit_num = []
moon_pos_rotated = []
inds = []
debug = False

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

for i in range(len(satX)):
    sat_pos = np.array([satX[i], satY[i], satZ[i]])
    moon_pos = np.array([moonX[i], moonY[i], moonZ[i]])
    
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
    rad = u/a # >> find radius of circle given u
    
    # >> test if moon is in cone (center of circle at x=0, y=0)
    dist = (moon_pos_rot[0]**2 + moon_pos_rot[1]**2)**0.5
    if dist <= rad and z >= 0:
        moonless_times.append(elapsed_secs[i])
        inds.append(i)
        if event_num[i] not in orbit_num: orbit_num.append(event_num[i])
    
        # >> debug on first moonless eclipse
        if len(inds) == 300: debug = True
        
    # -- plotting --------------------------------------------------------------
    # if i == 0: debug = True
    if debug:
        # >> cone parameters
        # >> radius of circle U/a = r_earth when z = mag(sat_pos) = u + sat_pos_z
        h = 400000.
        r_earth = 6371. # km
        a = (np.linalg.norm(sat_pos) - sat_pos[2]) / r_earth 
        angle = np.linspace(0, 2 * np.pi, 32)
        u = np.linspace(0, h, 32)
        theta, U = np.meshgrid(angle, u)
        
        # >> inverse rotate moon
        X = U * np.cos(theta) / a + sat_pos[0]
        Y = U * np.sin(theta) / a + sat_pos[1]
        Z = U + sat_pos[2]
        fig = plt.figure()
        ax = fig.gca(projection = '3d')
        ax.set_title('Rotated moon position, non-rotated cone: Orbit ' + str(i))
        ax.plot_surface(X, Y, Z, rstride =1, cstride = 1)
        ax.plot([sat_pos[0]], [sat_pos[1]], [sat_pos[2]], '.', label='satellite')
        ax.plot([sat_pos[0]], [sat_pos[1]], [0.], '.', label='earth') # >> rotated earth 
        moon_pos = np.resize(np.matmul(R_inv, np.array([[moonX[i]], [moonY[i]],
                             [moonZ[i]]])), (3))
        ax.plot([moon_pos[0]], [moon_pos[1]], [moon_pos[2]], '.', label = 'moon')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        
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
        ax1.set_title('Rotated cone, non-rotated moon: Orbit ' + str(i))
        ax1.plot_surface(X_rotated, Y_rotated, Z_rotated)
        ax1.plot([sat_pos[0]], [sat_pos[1]], [sat_pos[2]], '.', label='satellite')
        ax1.plot([0.], [0.], [0.], '.', label='earth')
        ax1.plot([moonX[i]], [moonY[i]], [moonZ[i]], '.', label='moon')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.set_zlabel('Z')
        ax1.legend()
        plt.show()
        
        debug = False

# # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 
# # testing 
# # fig1 = plt.figure()
# # ax1 = fig1.gca(projection = '3d')
# # ax1.plot([0, -sat_pos[0]], [0,-sat_pos[1]], [0, -sat_pos[2]], '-')
# # ax1.plot([0, 0], [0,0], [0, np.linalg.norm(sat_pos)], '-')
# # ax1.set_xlabel('X')
# # ax1.set_ylabel('Y')
# # ax1.set_zlabel('Z')
# # 
# # R = np.matrix(np.zeros((3,3)))
# # A = np.array([0, 0, 1])
# # B = -sat_pos / np.linalg.norm(sat_pos)
# # n = np.cross(A, B)
# # delt = np.matrix([[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]])
# # a, b, c = 1., 1., 1.# filler
# # for i in range(3):
# #     for j in range(3):
# #         R[i][j] = a*delt[i][j] + b*n[i]*n[j] + c*n
# 
# # A = np.array([0, 0, 1])
# # B = -sat_pos / np.linalg.norm(sat_pos)
# # G = np.matrix([[np.dot(A, B), -np.linalg.norm(np.cross(A, B)), 0.],
# #               [np.linalg.norm(np.cross(A, B)), np.dot(A,B), 0.],
# #               [0., 0., 1.]])
# # v = B - np.dot(A, B) * A
# # v = v / np.linalg.norm(v)
# # w = np.cross(B, A)
# # F = np.matrix([A, v, w])
# # U = np.linalg.inv(F) * G * F
# # vect_rotatd = np.array(np.matrix([0, 0, 1]) * U)[0]
# 
# # n = np.cross(np.array([-sat_pos[0], -sat_pos[1], -sat_pos[2]]),
# #              np.array([0, 0, np.linalg.norm(sat_pos)]))
# # d = np.dot(np.array([-sat_pos[0], -sat_pos[1], -sat_pos[2]]),
# #            np.array([0, 0, np.linalg.norm(sat_pos)]))
# # vcross = np.matrix([[0, -n[2], n[1]], [n[2], 0, -n[0]], [-n[1], n[0], 0]])
# # R = vcross + vcross*vcross*(1/(1+d))
# # vect_rotated = np.array(np.matrix(-sat_pos) * R)[0]
# # ax1.plot([0, vect_rotated[0]], [0, vect_rotated[1]], [0, vect_rotated[2]], '-')
# 
# # # transpose to reverse rotation
# # vect_rotated = np.array(np.matrix([0, 0, np.linalg.norm(sat_pos)]) * R)[0]
# # ax1.plot([0, vect_rotated[0]], [0, vect_rotated[1]], [0, vect_rotated[2]], '-')
# # 
# # vect_rotated1 = np.array(np.matrix(vect_rotated) * np.matrix.transpose(R))[0]
# # ax1.plot([0, vect_rotated1[0]], [0, vect_rotated1[1]], [0, vect_rotated1[2]], 'b-')
# 
# # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# 
# # a = np.array([0, 0, np.linalg.norm(sat_pos)])
# # b = np.array([-sat_pos[0], -sat_pos[1], -sat_pos[2]])
# # b = b / np.linalg.norm(b)
# # v = np.cross(a, b)
# # c = np.dot(a, b)
# # v_skewsym = np.matrix([[0, -v[2], v[1]], [v[2], 0, -v[0]], [-v[1], v[0], 0]])
# # I = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
# # R = I + v_skewsym * v_skewsym**2 * (1 / (1 + c))
# 
# #X = ((h - u) / h) * r * np.cos(theta)
# #Y = ((h - u) / h) * r * np.sin(theta)
# 
# # x = np.linspace(0,100,100)
# # y = np.linspace(0,100,100)
# # X,Y = np.meshgrid(x, y)
# # A = 3
# # B = 3
# # Z = (A**2*X**2 + B**2*Y**2)**0.5
# # z = (A**2*x**2 + B**2*y**2)**0.5
# # 
# # fig = plt.figure()
# # ax = fig.add_subplot(111, projection = '3d')
# # surf = ax.plot_surface(X, Y, Z, cmap = plt.cm.coolwarm, rstride = 1, cstride = 1)
# # plt.show()
# #ax.plot(x, y, z)
# 
# # fig = plt.figure()
# # ax = fig.gca(projection = '3d')
# # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
# # z = np.linspace(-2, 2, 100)
# # r = z**2 + 1
# # x = r * np.sin(theta)
# # y = r * np.cos(theta)
# # 
# # ax.plot(x, y, z)
# # plt.show()
# 
# # angle = np.linspace(0, 2*np.pi, 32)
# # theta, phi = np.meshgrid(angle, angle)
# # r, R = 0.25, 1.
# # X = (R + r * np.cos(phi)) * np.cos(theta)
# # Y = (R + r * np.cos(phi)) * np.sin(theta)
# # Z = r * np.sin(phi)
# # fig = plt.figure()
# # ax = fig.gca(projection = '3d')
# # ax.set_xlim3d(-1, 1)
# # ax.set_ylim3d(-1, 1)
# # ax.set_zlim3d(-1, 1)
# # ax.plot_surface(X, Y, Z, color = 'w', rstride = 1, cstride = 1)
# # plt.show()
# 
# # alpha = -np.arccos(np.dot(-sat_pos, np.array([1,0,0]))/np.linalg.norm(sat_pos))
# # beta  = -np.arccos(np.dot(-sat_pos, np.array([0,1,0]))/np.linalg.norm(sat_pos))
# # gamma = -np.arccos(np.dot(-sat_pos, np.array([0,0,1]))/np.linalg.norm(sat_pos))
# 
# 
# # :: testing code ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# sat_pos = np.array([satX[0], satY[0], satZ[0]])
# moon_pos = np.array([moonX[0], moonY[0], moonZ[0]])
# 
# h = 6000.
# # h = 3000. # >384400 dist to moon
# # >> radius of circle U/a = r_earth when z = mag(sat_pos) = u + sat_pos_z
# r_earth = 6371 # km
# a = (np.linalg.norm(sat_pos) - sat_pos[2]) / r_earth 
# angle = np.linspace(0, 2 * np.pi, 32)
# u = np.linspace(0, h, 32)
# theta, U = np.meshgrid(angle, u)
# 
# # >> make vertical cone
# X = U * np.cos(theta) / a + sat_pos[0]
# Y = U * np.sin(theta) / a + sat_pos[1]
# Z = U + sat_pos[2]
# 
# plt.ioff()
# fig1 = plt.figure()
# ax1 = fig1.gca(projection = '3d')
# ax1.plot_surface(X, Y, Z, rstride = 1, cstride = 1) # !!
# ax1.set_xlabel('X')
# ax1.set_ylabel('Y')
# ax1.set_zlabel('Z')
# # ax.plot([sat_pos[0]], [sat_pos[1]], [sat_pos[2]], '.') # !!
# # ax.plot([0], [0], [0], 'o') # >> position of earth # !!
# # >> find angles
# 
# # alpha: -angle between projection of vect on yz-plane and vect_rotated
# # beta: -angle between projection of vect on xz-plane and vect_rotated
# # vect_rotated_yz = -sat_pos * np.array([0, 1., 1.]) # projection onto yz plane
# # alpha = -np.arccos(np.dot(vect, vect_rotated_yz)/(np.linalg.norm(vect) * \
# #                                                np.linalg.norm(vect_rotated_yz)))
# # vect_rotated_xz = -sat_pos * np.array([1., 0, 1.]) # projection onto xz plane
# # beta = -np.arccos(np.dot(vect, vect_rotated_xz)/(np.linalg.norm(vect) * \
# #                                                np.linalg.norm(vect_rotated_xz)))                                    
# # vect_rotated_xy = -sat_pos * np.array([1., 1., 0.]) # projection onto xy plane
# # gam = -np.arccos(np.dot(vect, vect_rotated_xy)/(np.linalg.norm(vect) * \
# #                                                np.linalg.norm(vect_rotated_xy))) 
# 
# # alpha = np.radians(90)
# # beta = np.radians(0)
# # gam = np.radians(0)
# 
# # alpha > 0 rotates around y axis towards negative x
# # beta > 0 rotates around x axis towards negative y
# vect = np.array([0., 0., np.linalg.norm(sat_pos)])
# # # first rotate around y axis
# # vect_rotated_xz = -sat_pos * np.array([1., 0, 1.]) # projection onto xz plane
# # alpha = -np.arccos(np.dot(vect, vect_rotated_xz)/(np.linalg.norm(vect) * \
# #                                                 np.linalg.norm(vect_rotated_xz)))  
# # # now rotate around xaxis
# # vect_rotated_yz = -sat_pos * np.array([0, 1., 1.])
# # beta = np.arccos(np.dot(vect, vect_rotated_yz)/(np.linalg.norm(vect) * \
# #                                                 np.linalg.norm(vect_rotated_yz)))
# 
# # plt.figure()
# # plt.plot([0, vect[1]], [0, vect[2]], '-')
# # plt.plot([0, vect_rotated_yz[1]], [0, vect_rotated_yz[2]], '-')
# # plt.ylabel('z')
# # plt.xlabel('y')
# # 
# # plt.figure()
# # plt.plot([0, vect[0]], [0, vect[2]], '-')
# # plt.plot([0, vect_rotated_xz[0]], [0, vect_rotated_xz[2]], '-')
# # plt.ylabel('x')
# # plt.xlabel('z')
# # plt.show()
# 
# # >> gamma is always 0
# 
# alpha = np.radians(90)
# beta = np.radians(90)
# gamma = 0.
# 
# Rx = np.array([[1., 0., 0.], [0., np.cos(alpha), -np.sin(alpha)],
#                [0., np.sin(alpha), np.cos(alpha)]])
# Ry = np.array([[np.cos(beta), 0., np.sin(beta)], [0., 1., 0.],
#                 [-np.sin(beta), 0., np.cos(beta)]])
# Rz = np.array([[np.cos(gamma), -np.sin(gamma), 0.],
#                 [np.sin(gamma), np.cos(gamma), 0.], [0., 0., 1.]])
# # Rz = np.array([[0., 1., 0.], [-1., 0., 0.], [0., 0., 1.]])
# R = np.matmul(np.matmul(Rz, Ry), Rx)
#                
# X_rotated = np.zeros(np.shape(X))
# Y_rotated = np.zeros(np.shape(X))
# Z_rotated = np.zeros(np.shape(X))
# for i in range(np.shape(X)[0]):
#     for j in range(np.shape(Y)[0]):
#         vect = np.resize(np.array([X[i][j], Y[i][j], Z[i][j]]) - sat_pos, (3,1))
#         vect_rotated = np.matmul(R, vect) # (3x3)(3x1) = (3x1)
#         X_rotated[i][j], Y_rotated[i][j], Z_rotated[i][j] = \
#         np.resize(vect_rotated, (3)) + sat_pos
# ax1.plot_surface(X_rotated, Y_rotated, Z_rotated) # !!
# # ax.set_xlim3d(-7000, 0)
# # ax.set_ylim3d(1000, 8000)
# # ax.set_zlim3d(-6000, 1000)
# 
# # >> plot cone reference vectors
# ax1.plot([sat_pos[0], sat_pos[0]], [sat_pos[1], sat_pos[1]],
#         [sat_pos[2], sat_pos[2] + np.linalg.norm(sat_pos)], '-') # !!
# vect = np.array([0, 0, np.linalg.norm(sat_pos)])
# # vect_rotated = np.matmul(vect, R)
# vect = np.resize(vect, (3,1))
# vect_rotated = np.resize(np.matmul(R, vect), (3))
# 
# # print(vect_rotated)
# ax1.plot([sat_pos[0], vect_rotated[0] + sat_pos[0]],
#         [sat_pos[1], vect_rotated[1] + sat_pos[1]],
#         [sat_pos[2], vect_rotated[2] + sat_pos[2]], '-') # !!
# plt.show()
# 
# # ax.plot([0,-sat_pos[0]], [0, -sat_pos[1]], [0, -sat_pos[2]], '-')
# # ax.plot([sat_pos[0], 0], [sat_pos[1], 0], [sat_pos[2], 0], '-') #!!
# 
# # alpha = -alpha
# # beta = - beta
# # Rx1 = np.matrix([[1., 0., 0.], [0., np.cos(alpha), -np.sin(alpha)],
# #                [0., np.sin(alpha), np.cos(alpha)]])
# # Ry1 = np.matrix([[np.cos(beta), 0., np.sin(beta)], [0., 1., 0.],
# #                 [-np.sin(beta), 0., np.cos(beta)]])
# # Rz1 = np.matrix([[0., 1., 0.], [-1., 0., 0.], [0., 0., 1.]])
# # R1 = -R
# # vect_rotated1 = np.array(np.matrix(vect_rotated-sat_pos) * R1)[0]
# # ax.plot([sat_pos[0], vect_rotated1[0] + sat_pos[0]],
# #         [sat_pos[1], vect_rotated1[1] + sat_pos[1]],
# #         [sat_pos[2], vect_rotated1[2] + sat_pos[2]], '-')
# 
# 
# # >> calculate if moon_pos is within cone
# # X_rotated = X_rotated.flatten()
# # Y_rotated = Y_rotated.flatten()
# # Z_rotated = Z_rotated.flatten()
# 
#     vect = np.array([0., 0., np.linalg.norm(sat_pos)]) # >> initial v
#     
#     # >> first rotate around y axis
#     vect_rotated_xz = -sat_pos * np.array([1., 0, 1.]) # projection onto xz plane
#     alpha = -np.arccos(np.dot(vect, vect_rotated_xz)/(np.linalg.norm(vect) * \
#                                                 np.linalg.norm(vect_rotated_xz)))  
#     # >> now rotate around xaxis
#     vect_rotated_yz = -sat_pos * np.array([0, 1., 1.])
#     beta = np.arccos(np.dot(vect, vect_rotated_yz)/(np.linalg.norm(vect) * \
#                                                np.linalg.norm(vect_rotated_yz)))
#     
#     Rx = np.array([[1., 0., 0.], [0., np.cos(alpha), -np.sin(alpha)],
#                [0., np.sin(alpha), np.cos(alpha)]])
#     Ry = np.array([[np.cos(beta), 0., np.sin(beta)], [0., 1., 0.],
#                 [-np.sin(beta), 0., np.cos(beta)]])
#     Rz = np.array([[0., 1., 0.], [-1., 0., 0.], [0., 0., 1.]])
#     R = np.matmul(np.matmul(Rz, Ry), Rx)

# if debug:
#     # >> cone parameters
#     plt.ion()
#     h = 120000.
#     # h = 5000.
#     angle = np.linspace(0, 2 * np.pi, 32)
#     u = np.linspace(0, h, 32)
#     theta, U = np.meshgrid(angle, u)
# 
#     # >> make vertical cone
#     X = U * np.cos(theta) / a + sat_pos[0]
#     Y = U * np.sin(theta) / a + sat_pos[1]
#     Z = U + sat_pos[2]
# 
#     # >> plot cone
#     fig = plt.figure()
#     ax = fig.gca(projection = '3d')
#     # ax.plot_surface(X, Y, Z, rstride =1, cstride = 1) # !!
#     ax.set_xlabel('X')
#     ax.set_ylabel('Y')
#     ax.set_zlabel('Z')
#     
#     # >> plot rotated cone
#     X_rotated = np.zeros(np.shape(X))
#     Y_rotated = np.zeros(np.shape(X))
#     Z_rotated = np.zeros(np.shape(X))
#     for i in range(np.shape(X)[0]):
#         for j in range(np.shape(Y)[0]):
#             vect = np.resize(np.array([X[i][j], Y[i][j], Z[i][j]]) - sat_pos, (3,1))
#             vect_rotated = np.matmul(R, vect) # (3x3)(3x1) = (3x1)
#             X_rotated[i][j], Y_rotated[i][j], Z_rotated[i][j] = \
#             np.resize(vect_rotated, (3)) + sat_pos
#     ax.plot_surface(X_rotated, Y_rotated, Z_rotated)
#     
#     # >> plot points
#     # ax.plot([sat_pos[0]], [sat_pos[1]], [sat_pos[2]], '.', label = 'satellite') # !!
#     # ax.plot([0], [0], [0], 'o', label = 'earth')
#     # sax.plot([moonX[-1]], [moonY[-1]], [moonZ[-1]], 'o', label= 'moon')
#     plt.title('Orbit 80')
#     plt.legend()