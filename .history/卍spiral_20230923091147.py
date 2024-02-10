import numpy as np
import matplotlib.pyplot as plt
from draw_arc import *


def x_position(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def y_position(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)


for n in range(-10, 10):
    arc((x_position(n-1, 3*np.pi/4), y_position(n-1, 3*np.pi/4)),
        (x_position(n), y_position(n)), (x_position(n+1, np.pi/4), y_position(n+1, np.pi/4)), 'b')
# arc()
plt.show()
