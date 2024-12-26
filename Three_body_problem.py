# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 14:49:10 2024

@author: Mitch
"""

import math
import matplotlib.pyplot as plt

def update_point(body_0,body_1,mass_1,body_2,mass_2,velocity_0,time_step = 0.01,gravity = 1):
    distance_1 = ((body_0[0] - body_1[0]) ** 2 + \
                  (body_0[1] - body_1[1]) ** 2) ** (1/2)
    mag_acceleration_1 = gravity*mass_1/(distance_1 ** 2)
    speed_1 = mag_acceleration_1 * time_step
    angle_1 = math.atan2(body_0[1] - body_1[1], body_0[0] - body_1[0])
    velocity_1 = [-speed_1*math.cos(angle_1),-speed_1*math.sin(angle_1)]
    
    distance_2 = ((body_0[0] - body_2[0]) ** 2 + \
                  (body_0[1] - body_2[1]) ** 2) ** (1/2)
    mag_acceleration_2 = gravity*mass_2/(distance_2 ** 2)
    speed_2 = mag_acceleration_2 * time_step
    angle_2 = math.atan2(body_0[1] - body_2[1], body_0[0] - body_2[0])
    velocity_2 = [-speed_2*math.cos(angle_2),-speed_2*math.sin(angle_2)]
    
    velocity_axis_0 = velocity_0[0] + velocity_1[0] + velocity_2[0]
    velocity_axis_1 = velocity_0[1] + velocity_1[1] + velocity_2[1]
    velocity = [velocity_axis_0,velocity_axis_1]
    
    movement = [v * time_step for v in velocity]
    
    body_0_final_axis_0 = body_0[0] + movement[0]
    body_0_final_axis_1 = body_0[1] + movement[1]
    body_0_final = [body_0_final_axis_0,body_0_final_axis_1]
    
    return [body_0_final,velocity]

def update_all(body_0,velocity_0,mass_0,body_1,velocity_1,mass_1,body_2,velocity_2,mass_2):
    body_0_newpos = \
        update_point(body_0[-1], body_1[-1], mass_1, body_2[-1], mass_2, velocity_0[-1])[0]
    body_0_newvelocity = \
        update_point(body_0[-1], body_1[-1], mass_1, body_2[-1], mass_2, velocity_0[-1])[1]
        
    body_1_newpos = \
        update_point(body_1[-1], body_0[-1], mass_0, body_2[-1], mass_2, velocity_1[-1])[0]
    body_1_newvelocity = \
        update_point(body_1[-1], body_0[-1], mass_0, body_2[-1], mass_2, velocity_1[-1])[1]
    
    body_2_newpos = \
        update_point(body_2[-1], body_1[-1], mass_1, body_0[-1], mass_0, velocity_2[-1])[0]
    body_2_newvelocity = \
        update_point(body_2[-1], body_1[-1], mass_1, body_0[-1], mass_0, velocity_2[-1])[1]
    
    
    body_0.append(body_0_newpos)
    velocity_0.append(body_0_newvelocity)
    
    body_1.append(body_1_newpos)
    velocity_1.append(body_1_newvelocity)
    
    body_2.append(body_2_newpos)
    velocity_2.append(body_2_newvelocity)
    
    return body_0,velocity_0,body_1,velocity_1,body_2,velocity_2

def loop_it(body_0,velocity_0,mass_0,body_1,velocity_1,mass_1,body_2,velocity_2,mass_2,ntimes = 50):
    n = 0
    while n <= ntimes:
        body_0,velocity_0,body_1,velocity_1,body_2,velocity_2 = \
            update_all(body_0,velocity_0,mass_0,body_1,velocity_1,mass_1,body_2,velocity_2,mass_2)
        n += 1
    
    body_0_x = [coord[0] for coord in body_0]
    body_0_y = [coord[1] for coord in body_0]
    
    body_1_x = [coord[0] for coord in body_1]
    body_1_y = [coord[1] for coord in body_1]
    
    body_2_x = [coord[0] for coord in body_2]
    body_2_y = [coord[1] for coord in body_2]
    
    return body_0_x, body_0_y, body_1_x, body_1_y, body_2_x, body_2_y

def plot_it(body_0,velocity_0,mass_0,body_1,velocity_1,mass_1,body_2,velocity_2,mass_2,ntimes = 50):
    body_0_x, body_0_y, body_1_x, body_1_y, body_2_x, body_2_y = \
        loop_it(body_0,velocity_0,mass_0,body_1,velocity_1,mass_1,body_2,velocity_2,mass_2,ntimes)
    
    plt.figure()
    plt.plot(body_0_x,body_0_y,body_1_x,body_1_y,body_2_x,body_2_y)
    plt.grid()
    plt.show
