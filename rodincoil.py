import numpy as np
import matplotlib.pyplot as plt
from circle import *

# R = 1
# r = 2*R
# for n in range(0, 12):
#     circle((R*np.cos(n*np.pi/6), R*np.sin(n*np.pi/6)), r)


def rodincoil(R, r, n, color='b', theta=0):
    for i in range(0, n):
        circle((R*np.cos(i*2*np.pi/n+theta), R *
               np.sin(i*2*np.pi/n+theta)), r, color)


def rodincoil_colorful(R, r, n, colors, theta=0):
    for i in range(0, n):
        circle((R*np.cos(i*2*np.pi/n+theta), R *
               np.sin(i*2*np.pi/n+theta)), r, colors[i])


# rodincoil(1, 2, 6, 'r')
# rodincoil_colorful(1, 2, 6, ['r', 'g', 'b', 'y', 'm', 'c'])
# # circle((0, 0), 1, 'g')
# plt.axis('equal')
# plt.show()
