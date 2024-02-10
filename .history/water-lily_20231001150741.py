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


def waterlily_x_center_inverse(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+7*np.pi/4+thelta)


def waterlily_y_center_inverse(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+7*np.pi/4+thelta)


# from:
def waterlily_x_from(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def waterlily_y_from(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)


# to
(0, 0)
