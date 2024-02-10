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

def onepetal(n, thelta, color):
    arc((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)), (0, 0),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)
    arc((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), (0, 0), color)


# 颜色：红橙黄绿蓝靛紫
color = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'w']
# petals
# for i in range(-8, 8):
#     onepetal(i, color[i])
for n in range(-8, 8):
    for i in range(0, 25):
        onepetal(n, i*np.pi/12, 'g')
# onepetal(7, 'g')

# water-lily


# for alpha in range(0, 12):
#     for n in range(-10, 9):
#         arc_inverse((loutus_x_center_inverse(n, alpha*np.pi/6), loutus_y_center_inverse(n, alpha*np.pi/6)),
#                     (loutus_x_from_inverse(n, alpha*np.pi/6),
#                      loutus_y_from_inverse(n, alpha*np.pi/6)),
#                     (loutus_x_to_inverse(n, alpha*np.pi/6), loutus_y_to_inverse(n, alpha*np.pi/6)), 'y')


plt.axis('equal')
plt.show()
