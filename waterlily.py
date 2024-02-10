import numpy as np
import matplotlib.pyplot as plt
from arc import *
# from arc_fill import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

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


# 聚
def onepetal(n, thelta, color):
    arc((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)), (0, 0),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)
    arc((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), (0, 0), color)


# 放
def onepetal_open(n, thelta, color):
    arc_inverse((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)),
                (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)),  (0, 0), color)
    arc_inverse((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)), (0, 0),
                (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)


# 颜色：红橙黄绿蓝靛紫
color = ['r', 'g', 'c', 'purple', 'b', 'g', '#FFFF00', 'r']
# petals
# for i in range(-8, 8):
#     onepetal(i, color[i])
# onepetal(7, 'g')

# water-lily

# for n in range(7, 0, -1):
#     for i in range(0, 13):
#         onepetal(n, i*np.pi/6, color[n])
# onepetal_open(n, i*np.pi/6, color[n])

# plt.axis('equal')
# plt.show()

# 填充


# def onepetal_fill(n, thelta, color):
#     arc_fill((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)), (0, 0),
#              (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)
#     arc_fill((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)),
#              (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), (0, 0), color)

# 根号3的花
def onearc_lotus_3(center, r, theta, color='b'):
    # arc_degree((0, 0), r, theta, theta+2*np.pi/3, 'r')
    arc_degree_inverse(center, r, theta, theta+2*np.pi/3, color)


def lotus_3(r, n, theta=0, color='b'):
    for i in range(0, n+1):
        onearc_lotus_3((r*np.cos(i*2*np.pi/n+theta),
                       r*np.sin(i*2*np.pi/n+theta)), r, theta+i*2*np.pi/n-2*np.pi/6, color)


# 8瓣花

def onearc_lotus_8(center, r, theta, color='b'):
    # arc_degree((0, 0), r, theta, theta+2*np.pi/3, 'r')
    arc_degree_inverse(center, r, theta, theta+3*np.pi/4, color)


def lotus_8(r, n, theta=0, color='b'):
    for i in range(0, n+1):
        onearc_lotus_3((r*np.cos(i*2*np.pi/n+theta),
                       r*np.sin(i*2*np.pi/n+theta)), r, theta+i*2*np.pi/n-2*np.pi/8-2*i*np.pi, color)

#
#
#


# def onearc_lotus_n(center, r, n, theta, color='b'):
#     arc_degree(center, r, theta, theta+2*np.pi*(n-2)/n, color)
#     # (n-2)/n个圆弧
#     # arc_degree_inverse(center, r, theta, theta+2*np.pi*(n-2)/n, color)


# def lotus_n(r, n, theta=0, color='b'):
#     for i in range(0, n+1):
#         onearc_lotus_n((r*np.cos(i*2*np.pi/n+np.pi/2+theta),
#                        r*np.sin(i*2*np.pi/n+np.pi/2+theta)), r, n, theta+i*2*np.pi/n, color)


# for i in range(2):
#     lotus_3(np.sqrt(3)**i, 12, i*np.pi/6, 'r')
# lotus_3(1)
# lotus_3(np.sqrt(3))

# lotus_n(1, 4, 0)
# # lotus_8(1, 8, 0)
# # onearc_lotus_8((0, 0), 1, 0, color='b')
# # onearc_lotus_n((0, 0), 1, 5, 2*np.pi/5)
# # onearc_lotus_3((0, 0), 1, -np.pi/3)
# plt.show()
