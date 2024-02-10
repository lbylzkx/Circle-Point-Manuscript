import numpy as np
import matplotlib.pyplot as plt
from arc import *


# points of water-lily

# Right:
# center:
def waterlily_x_center_right(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+np.pi/4+thelta)


def waterlily_y_center_right(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+np.pi/4+thelta)


# Left:
# center:


def waterlily_x_center_left(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+7*np.pi/4+thelta)


def waterlily_y_center_left(n, thelta=0):
    return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+7*np.pi/4+thelta)


# from:
def waterlily_x_from(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def waterlily_y_from(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)


# to
(0, 0)


# petal
# 放
# arc_inverse((waterlily_x_center_left(8), waterlily_y_center_left(8)),
#             (waterlily_x_from(8), waterlily_y_from(8)), (0, 0), 'g')
# arc_inverse((waterlily_x_center_right(8), waterlily_y_center_right(8)), (0, 0),
#             (waterlily_x_from(8), waterlily_y_from(8)), 'g')
# 聚
# arc((waterlily_x_center_left(8), waterlily_y_center_left(8)), (0, 0),
#     (waterlily_x_from(8), waterlily_y_from(8)))
# arc((waterlily_x_center_right(8), waterlily_y_center_right(8)),
#     (waterlily_x_from(8), waterlily_y_from(8)), (0, 0))

def onepetal(n, color):
    arc((waterlily_x_center_left(n), waterlily_y_center_left(n)), (0, 0),
        (waterlily_x_from(n), waterlily_y_from(n)), color)
    arc((waterlily_x_center_right(n), waterlily_y_center_right(n)),
        (waterlily_x_from(n), waterlily_y_from(n)), (0, 0), color)


# 颜色：红橙黄绿蓝靛紫
color = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
# petals
for i in range(-8, 8):
    onepetal(i, color[i])

# for n in range(-10, 9):
onepetal(7, 'g')
plt.axis('equal')
plt.show()
