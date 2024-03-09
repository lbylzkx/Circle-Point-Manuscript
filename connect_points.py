from points import *
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

# 首尾连接


def connect(points, color='g'):
    num = len(points)
    for i in range(-1, num-1):
        plt.plot([points[i][0], points[i+1][0]],
                 [points[i][1], points[i+1][1]], color)


def connect_in_order(points, color='g'):
    num = len(points)
    for i in range(0, num-1):
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

# 多重多边形


def multi_polygon(n, m, color='b', alpha=0, theta=0):
    for i in range(m):
        connect(n_points(n, (np.cos(np.pi/n)) **
                (-i), alpha+i*(np.pi/n+theta)), color)

# 类梅塔特隆立方体连接


def connect_like_metatron(n, m, color='b', theta=0):
    points = []
    for i in range(m):
        points += n_points(n, i+1, theta)
    connect_all(points, color)

# 卍字连接


def draw_swastika(n, R, theta=0, color='b'):
    if n == 2:
        for i in range(4):
            plt.plot([R*np.sqrt(2)**(n-2)*np.cos(i*2*np.pi/4+theta), 0],
                     [R*np.sqrt(2) ** (n-2)*np.sin(i*2*np.pi/4+theta), 0], color)
    elif n % 2 == 1:
        for i in range(4):
            plt.plot([R*np.sqrt(2)**(n-3)*np.cos(i*2*np.pi/4+theta), 0],
                     [R*np.sqrt(2) ** (n-3)*np.sin(i*2*np.pi/4+theta), 0], color)
            plt.plot([R*np.sqrt(2)**(n-2)*np.cos(i*2*np.pi/4+np.pi/4+theta), 0],
                     [R*np.sqrt(2) ** (n-2)*np.sin(i*2*np.pi/4+np.pi/4+theta), 0], color)
    else:
        for i in range(4):
            plt.plot([R*np.sqrt(2)**(n-2)*np.cos(i*2*np.pi/4+theta), 0],
                     [R*np.sqrt(2) ** (n-2)*np.sin(i*2*np.pi/4+theta), 0], color)
            plt.plot([R*np.sqrt(2)**(n-3)*np.cos(i*2*np.pi/4+np.pi/4+theta), 0],
                     [R*np.sqrt(2) ** (n-3)*np.sin(i*2*np.pi/4+np.pi/4+theta), 0], color)
    for i in range(4):
        points = swastika(n, R, i*2*np.pi/4+theta)
        connect_in_order(points, color)


def draw_swastikas(n, R, m, color='b', theta=0):
    for i in range(m):
        draw_swastika(n, R, i*np.pi/m+theta, color)


# draw_swastikas(12, 1, 32, 'r')
# draw_swastika(5, 4, 1, 0)
# connect_in_order(swastika(4, 1), 'r')
# connect(points)
# connect_all(n_points(5, 1))
# connect_all_with_points(n_points(10, 2), 'r')
# connect(n_points(5, 1))
# connect_with_points(n_points(5, 2))


# plt.axis('equal')
# plt.show()
