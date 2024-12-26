import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import Three_body_problem as Threebod

# %matplotlib qt

plt.rcParams["figure.figsize"] = 4,3

mass_0, body_0, velocity_0 = [10, [[0,0]],[[0,0]]]
mass_1, body_1, velocity_1 = [2, [[-15,0]],[[0.5,-0.5]]]
mass_2, body_2, velocity_2 = [2, [[0,-15]],[[0.5,0]]]

ntimes = 100000
size = 40
density = 1

body_0_x, body_0_y, body_1_x, body_1_y, body_2_x, body_2_y = \
    Threebod.loop_it(body_0,velocity_0,mass_0,body_1,velocity_1,mass_1,body_2,velocity_2,mass_2,ntimes)
def firstbody(phi):
    xpos = body_0_x[phi]
    ypos = body_0_y[phi]
    return np.array([xpos, ypos])

def secondbody(phi):
    xpos = body_1_x[phi]
    ypos = body_1_y[phi]
    return np.array([xpos, ypos])

def thirdbody(phi):
    xpos = body_2_x[phi]
    ypos = body_2_y[phi]
    return np.array([xpos, ypos])

# create a figure with an axes
fig, ax = plt.subplots()
# set the axes limits
ax.axis([-size,size,-size,size])
# set equal aspect such that the circle is not shown as ellipse
ax.set_aspect("equal")
# create a point in the axes
point1, = ax.plot(0,1, marker="o", markersize = (size*density*mass_0)/25)
point2, = ax.plot(0,1, marker="o", markersize = (size*density*mass_1)/25)
point3, = ax.plot(0,1, marker="o", markersize = (size*density*mass_2)/25)

# Updating function, to be repeatedly called by the animation
def update(phi):
    # obtain point coordinates 
    x1, y1 = firstbody(phi)
    x2, y2 = secondbody(phi)
    x3, y3 = thirdbody(phi)
    # set point's coordinates
    point1.set_data(x1, y1)
    point2.set_data(x2, y2)
    point3.set_data(x3, y3)
    return point1, point2, point3

# create animation with 10ms interval, which is repeated
Frames = np.linspace(0,ntimes,ntimes, endpoint=False,dtype=int)
ani = FuncAnimation(fig, update, interval=1, blit=True, repeat=True,
                    frames=Frames)

plt.show()