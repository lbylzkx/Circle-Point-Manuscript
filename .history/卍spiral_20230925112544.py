import numpy as np
import matplotlib.pyplot as plt
from arc import *


# The points of 卍 or lotus

# center:
def loutus_x_center(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos((n-1)*np.pi/4-np.pi/4)


def loutus_y_center(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin((n-1)*np.pi/4-np.pi/4)


# from:
def x_position(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def y_position(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)

# to:


def loutus_x_to(n):
    return np.sqrt(2)**(n+1)*np.cos((n+1)*np.pi/4+np.pi/4)


def loutus_y_to(n):
    return np.sqrt(2)**(n+1)*np.sin((n+1)*np.pi/4+np.pi/4)


# for n in range(-10, 10):
#     arc((x_position(n-1, 3*np.pi/4), y_position(n-1, 3*np.pi/4)),
#         (x_position(n), y_position(n)), (x_position(n+1, np.pi/4), y_position(n+1, np.pi/4)), 'b')
# arc()
# plt.axis('equal')
# plt.show()
