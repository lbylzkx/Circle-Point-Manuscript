import numpy as np
import matplotlib.pyplot as plt
from arc import *


# The points of 卍 or lotus

# center:
def loutus_x_center(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+3*np.pi/4+thelta)


def loutus_y_center(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+3*np.pi/4+thelta)


# from:
def x_position(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def y_position(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)

# to:


def loutus_x_to(n, thelta=0):
    return np.sqrt(2)**(n+1)*np.cos(n*np.pi/4+np.pi/4+thelta)


def loutus_y_to(n, thelta=0):
    return np.sqrt(2)**(n+1)*np.sin(n*np.pi/4+np.pi/4+thelta)


# for n in range(-10, 10):
#     arc((x_position(n-1, 3*np.pi/4), y_position(n-1, 3*np.pi/4)),
#         (x_position(n), y_position(n)), (x_position(n+1, np.pi/4), y_position(n+1, np.pi/4)), 'b')

for alpha in range(0, 4):
    for n in range(-10, 9):
        arc((loutus_x_center(n, alpha*np.pi/2), loutus_y_center(n, alpha*np.pi/2)),
            (x_position(n, alpha*np.pi/2), y_position(n, alpha*np.pi/2)), (loutus_x_to(n, alpha*np.pi/2), loutus_y_to(n, alpha*np.pi/2)))

plt.axis('equal')
plt.show()
