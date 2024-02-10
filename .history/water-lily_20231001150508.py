import numpy as np
import matplotlib.pyplot as plt
from arc import *


# points of water-lily

# center:
def x_position_waterlily(n):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+np.pi/4)


def y_position_waterlily(n):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+np.pi/4)

#


def loutus_x_center_inverse(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+7*np.pi/4+thelta)


def loutus_y_center_inverse(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+7*np.pi/4+thelta)


# from:
# x_position()
# y_position()
# to
(0, 0)
