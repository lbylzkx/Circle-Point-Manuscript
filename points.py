from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np
import os
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


# # 获取文件的父目录
# parent_dir = os.path.dirname(os.path.abspath(__file__))

# # 将父目录添加到sys.path中
# sys.path.append(parent_dir)


# # points generated in progression


# def get_x_n(i):
#     if i == 1:
#         return 1
#     else:
#         return get_x_n(i-1)+4


# def get_y_n(i):
#     if i == 1:
#         return 1
#     else:
#         return get_y_n(i-1)+3


# def two(n):
#     return 1/2**n


# def x_squence(i):
#     n = get_x_n(i)
#     return [-two(n-1), 0, two(n), two(n), two(n+1), 0, -two(n+2), -two(n+2)]


# def y_squence(i):
#     n = get_y_n(i)
#     return [two(n-1), two(n-1), two(n), 0, -two(n+1), -two(n+1), -two(n+2), 0]


# # Tests
# # print(two(1),two(2),two(3),two(4),two(5))
# # while True:
# #     n = int(input("Enter cycles:"))
# #     x_all = []
# #     for i in range(n):
# #         x_i = x_squence(i+1)
# #         x_all = x_all + [x_i]
# #     x = [element for sublist in x_all for element in sublist]
# #     # print(x)

# #     y_all = []
# #     for i in range(n):
# #         y_i = y_squence(i+1)
# #         y_all = y_all + [y_i]
# #     y = [element for sublist in y_all for element in sublist]
# #     # print(y)

# #     """
# #     see in Fraction
# #     """
# #     # x = x_squence(n)
# #     # y = y_squence(n)
# #     for i, a in enumerate(x):
# #         x[i] = Fraction(a).limit_denominator()
# #     for i, a in enumerate(y):
# #         y[i] = Fraction(a).limit_denominator()
# #     print(x)
# #     print(y)
# #     plt = plt.plot(x, y)


# # generrate points by 三角函数

# def x_position(n, thelta=0):
#     return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


# def y_position(n, thelta=0):
#     return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)


# # Tests
# x = [x_position(i, thelta=0) for i in range(-10, 10)]
# y = [y_position(i, thelta=0) for i in range(-10, 10)]

# for i, a in enumerate(x):
#     x[i] = Fraction(a).limit_denominator()

# print(x)


# # The points of 卍 or lotus

# # center:
# def loutus_x_center(n):
#     return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4-np.pi/4)


# def loutus_y_center(n):
#     return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4-np.pi/4)


# # from:
# x_position()
# y_position()

# # to:


# def loutus_x_to(n):
#     return np.sqrt(2)**(n+1)*np.cos((n+1)*np.pi/4+np.pi/4)


# def loutus_y_to(n):
#     return np.sqrt(2)**(n+1)*np.sin((n+1)*np.pi/4+np.pi/4)


# # points of water-lily

# # center:
# def x_position_waterlily(n):
#     return np.sqrt(2)**(n-1)*np.cos(n*np.pi/4+np.pi/4)


# def y_position_waterlily(n):
#     return np.sqrt(2)**(n-1)*np.sin(n*np.pi/4+np.pi/4)


# # from:
# x_position()
# y_position()
# # to
# (0, 0)

# 生成半径R圆上均匀N等分点
def n_points(N, R, theta=0):
    return [[R*np.cos(i*2 * np.pi/N+np.pi/2+theta), R*np.sin(i*2 * np.pi/N+np.pi/2+theta)] for i in range(N)]

# 画出点


def draw_points(points, colorp='b', size=100):
    for i in range(len(points)):
        plt.scatter(points[i][0], points[i][1], s=size, color=colorp)

# 双向生成点阵


def n_points_array(n, m, theta=0):
    points = []
    for i in range(m):
        points += n_points(n, np.sqrt(2*np.cos(np.pi/n))**i, i*(np.pi/n+theta))
        points += n_points(n, np.sqrt(2*np.cos(np.pi/n))
                           ** (-i), i*(np.pi/n-theta))
    return points


# 向内生成点阵
def n_points_array_inner(n, m, theta=0):
    points = []
    for i in range(m):
        points += n_points(n, np.sqrt(2*np.cos(np.pi/n))
                           ** (-i-1), i*(np.pi/n+theta))
    return points


# 向外生成点阵
def n_points_array_outer(n, m, theta=0):
    points = []
    for i in range(m):
        points += n_points(n, np.sqrt(2*np.cos(np.pi/n))**i, i*(np.pi/n+theta))
    return points
# 画N边形点阵
# n:边数
# m: 阵列层数


def draw_n_points_array(n, m, theta=0, color='b', size=100):
    for i in range(m):
        draw_points(
            n_points(n, np.sqrt(2*np.cos(np.pi/n))**i, i*(np.pi/n+theta)), color, size)
        draw_points(
            n_points(n, np.sqrt(2*np.cos(np.pi/n))**(-i), i*(np.pi/n-theta)), color, size)

# 向外画点阵


def draw_n_points_array_outer(n, m, theta=0, color='b', size=100):
    for i in range(m):
        draw_points(
            n_points(n, np.sqrt(2*np.cos(np.pi/n))**i, i*(np.pi/n+theta)), color, size)

# 向内画点阵


def draw_n_points_array_inner(n, m, theta=0, color='b', size=100):
    for i in range(m):
        draw_points(
            n_points(n, np.sqrt(2*np.cos(np.pi/n))**(-i-1), i*(np.pi/n-theta)), color, size)

# draw_points(n_points(16, 1))
# draw_points(n_points(6, 1/2, np.pi), 300, 'g')


# draw_points(n_points_array(8, 3, np.pi/3), 'g', 300)
# draw_n_points_array(8, 3, np.pi/3)

# draw_points(n_points_array_outer(8, 3, np.pi/3), 'g', 300)
# draw_n_points_array_outer(8, 3, np.pi/3, 'r')
# draw_points(n_points_array_inner(12, 3, -np.pi/3), 'g', 300)
# draw_n_points_array_inner(12, 3, -np.pi/3, 'b')
# plt.axis('equal')
# plt.show()
