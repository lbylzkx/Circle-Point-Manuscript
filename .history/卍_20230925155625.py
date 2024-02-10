import numpy as np
import matplotlib.pyplot as plt
from arc import *
from 卍spiral import *


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

# for alpha in range(0, 4):
#     for n in range(-10, 9):
#         arc((loutus_x_center(n, alpha*np.pi/2), loutus_y_center(n, alpha*np.pi/2)),
#             (x_position(n, alpha*np.pi/2), y_position(n, alpha*np.pi/2)), (loutus_x_to(n, alpha*np.pi/2), loutus_y_to(n, alpha*np.pi/2)))


arc((loutus_x_center_inverse(8, np.pi/2), loutus_y_center_inverse(8, np.pi/2)),
    (x_position_inverse(8, np.pi/2), y_position_inverse(8, np.pi/2)), (loutus_x_to_inverse(8, np.pi/2), loutus_y_to_inverse(8, np.pi/2)), 'r')

# arc((-8, 8), (16, 0), (16

plt.axis('equal')
plt.show()
