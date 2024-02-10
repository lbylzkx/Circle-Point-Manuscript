import numpy as np
import matplotlib.pyplot as plt
from arc import *
from points import *


def x_position(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def y_position(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)


# axis
x_axis_1 = [x_position(8), x_position(8, thelta=np.pi)]
y_axis_1 = [y_position(8), y_position(8, thelta=np.pi)]
plt.plot(x_axis_1, y_axis_1, 'b')

x_axis_2 = [x_position(8, thelta=np.pi/2), x_position(8, thelta=3*np.pi/2)]
y_axis_2 = [y_position(8, thelta=np.pi/2), y_position(8, thelta=3*np.pi/2)]
plt.plot(x_axis_2, y_axis_2, 'b')

x_axis_3 = [x_position(7, thelta=0), x_position(7, thelta=np.pi)]
y_axis_3 = [y_position(7, thelta=0), y_position(7, thelta=np.pi)]
plt.plot(x_axis_3, y_axis_3, 'b')

x_axis_4 = [x_position(7, thelta=np.pi/2), x_position(7, thelta=3*np.pi/2)]
y_axis_4 = [y_position(7, thelta=np.pi/2), y_position(7, thelta=3*np.pi/2)]
plt.plot(x_axis_4, y_axis_4, 'b')
# axis

x1 = [x_position(i, thelta=0) for i in range(-10, 10)]
y1 = [y_position(i, thelta=0) for i in range(-10, 10)]
plt.plot(x1, y1, 'b')

x2 = [x_position(i, thelta=np.pi/2) for i in range(-10, 10)]
y2 = [y_position(i, thelta=np.pi/2) for i in range(-10, 10)]
plt.plot(x2, y2, 'b')

x3 = [x_position(i, thelta=np.pi) for i in range(-10, 10)]
y3 = [y_position(i, thelta=np.pi) for i in range(-10, 10)]
plt.plot(x3, y3, 'b')

x4 = [x_position(i, thelta=3*np.pi/2) for i in range(-10, 10)]
y4 = [y_position(i, thelta=3*np.pi/2) for i in range(-10, 10)]
plt.plot(x4, y4, 'b')

# for n in range(-10, 8):
#     arc((x_position(n-1, 3*np.pi/4), y_position(n-1, 3*np.pi/4)),
#         (x_position(n), y_position(n)), (x_position(n+1, np.pi/4), y_position(n+1, np.pi/4)), 'b')


arc((loutus_x_center(8)), loutus_y_center(8),
    (x_position(8), y_position(8)), (x_position(9, np.pi/4), y_position(9, np.pi/4)),)

# arc((-8, 8), (16, 0), (16, 16))

plt.axis('equal')
plt.show()
