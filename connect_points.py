import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

# N = 12
# R = 10
# points = [[R*np.cos(i*2 * np.pi/N), R*np.sin(i*2 * np.pi/N)] for i in range(N)]

# 生成半径R圆上N等分点


def n_points(N, R, theta=0):
    return [[R*np.cos(i*2 * np.pi/N+np.pi/2+theta), R*np.sin(i*2 * np.pi/N+np.pi/2+theta)] for i in range(N)]


# 两两连接所有点


def connect_all(points, color='g'):
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            plt.plot([points[i][0], points[j][0]],
                     [points[i][1], points[j][1]], color)


# 带点两两连接所有点
def connect_all_with_points(points, colorp='b', colorl='g'):
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            plt.plot([points[i][0], points[j][0]],
                     [points[i][1], points[j][1]], colorl)
    for i in range(len(points)):
        plt.scatter(points[i][0], points[i][1], color=colorp)

# 首位连接


def connect(points, color='g'):
    num = len(points)
    for i in range(-1, num-1):
        plt.plot([points[i][0], points[i+1][0]],
                 [points[i][1], points[i+1][1]], color)

# 带点首位连接


def connect_with_points(points, colorp='b', colorl='g'):
    num = len(points)
    for i in range(-1, num-1):
        plt.plot([points[i][0], points[i+1][0]],
                 [points[i][1], points[i+1][1]], colorl)
    for i in range(len(points)):
        plt.scatter(points[i][0], points[i][1], color=colorp)


# connect(points)
# connect_all(n_points(5, 1))
# connect_all_with_points(n_points(10, 2), 'r')
# connect(n_points(5, 1))
# connect_with_points(n_points(5, 2))

# plt.axis('equal')
# plt.show()
