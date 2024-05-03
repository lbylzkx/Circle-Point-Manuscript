import numpy as np
import matplotlib.pyplot as plt
from arc import *
from lotus import *
from waterlily import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def onepetal_ll(n, thelta, color):
    arc((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)), (0, 0),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)
    arc((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), (0, 0), color)
    arc((loutus_x_center(n, thelta), loutus_y_center(n, thelta)),
        (loutus_x_from(n, thelta), loutus_y_from(n, thelta)),
        (loutus_x_to(n, thelta), loutus_y_to(n, thelta)), color)
    arc((loutus_x_center_inverse(n, thelta), loutus_y_center_inverse(n, thelta)),
        (loutus_x_to_inverse(n, thelta), loutus_y_to_inverse(n, thelta)),
        (loutus_x_from_inverse(n, thelta), loutus_y_from_inverse(n, thelta)), color)

# 正spiral


def onepetal_spiral(n, thelta, color):
    arc((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)), (0, 0),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)
    arc((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), (0, 0), color)
    arc((loutus_x_center(n, thelta), loutus_y_center(n, thelta)),
        (loutus_x_from(n, thelta), loutus_y_from(n, thelta)),
        (loutus_x_to(n, thelta), loutus_y_to(n, thelta)), color)
# 逆spiral


def onepetal_spiral_i(n, thelta, color):
    arc((waterlily_x_center_left(n, thelta), waterlily_y_center_left(n, thelta)), (0, 0),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), color)
    arc((waterlily_x_center_right(n, thelta), waterlily_y_center_right(n, thelta)),
        (waterlily_x_from(n, thelta), waterlily_y_from(n, thelta)), (0, 0), color)
    arc((loutus_x_center_inverse(n, thelta), loutus_y_center_inverse(n, thelta)),
        (loutus_x_to_inverse(n, thelta), loutus_y_to_inverse(n, thelta)),
        (loutus_x_from_inverse(n, thelta), loutus_y_from_inverse(n, thelta)), color)


# onepetal_spiral(1, 0, 'r')
color = ['r', 'g', 'b']*8
color1 = ['r', 'orange', 'y', 'g', 'cyan', 'b']*4
# for n in range(7, 0, -1):
#     for i in range(0, 13):
#         onepetal_spiral(n, i*np.pi/6, color1[i])

# plt.axis('equal')
# plt.show()
