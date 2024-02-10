import numpy as np
import matplotlib.pyplot as plt
from arc import *


# The points of 卍 or lotus

# 正旋(右旋)
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

# 逆旋(左旋)
# center:


def loutus_x_center_inverse(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+7*np.pi/4+thelta)


def loutus_y_center_inverse(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+7*np.pi/4+thelta)


# from:
def x_position_inverse(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/2+thelta)


def y_position_inverse(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/2+thelta)

# to:


def loutus_x_to_inverse(n, thelta=0):
    return np.sqrt(2)**(n+1)*np.cos(n*np.pi/4+np.pi/4+thelta)


def loutus_y_to_inverse(n, thelta=0):
    return np.sqrt(2)**(n+1)*np.sin(n*np.pi/4+np.pi/4+thelta)


for alpha in range(0, 4):
    for n in range(-10, 9):
        arc((loutus_x_center(n, alpha*np.pi/2), loutus_y_center(n, alpha*np.pi/2)),
            (x_position(n, alpha*np.pi/2), y_position(n, alpha*np.pi/2)), (loutus_x_to(n, alpha*np.pi/2), loutus_y_to(n, alpha*np.pi/2)), 'r')
        # arc((loutus_x_center_inverse(n, alpha*np.pi/2), loutus_y_center_inverse(n, alpha*np.pi/2)),
        #     (x_position_inverse(n, alpha*np.pi/2), y_position_inverse(n, alpha*np.pi/2)), (loutus_x_to_inverse(n, alpha*np.pi/2), loutus_y_to_inverse(n, alpha*np.pi/2)), 'r')
arc((loutus_x_center_inverse(8, alpha*np.pi/2), loutus_y_center_inverse(8, alpha*np.pi/2)),
    (x_position_inverse(8, alpha*np.pi/2), y_position_inverse(8, alpha*np.pi/2)), (loutus_x_to_inverse(8, alpha*np.pi/2), loutus_y_to_inverse(8, alpha*np.pi/2)), 'r')
plt.axis('equal')
plt.show()
