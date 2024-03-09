import numpy as np
import matplotlib.pyplot as plt
from arc import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

# 花弧


def onearc_lily_n(center, r, n, theta, color='b'):
    # (n-2)/n个圆弧
    arc_degree(center, r, theta, theta+2*np.pi*(n-2)/n, color)


def onearc_lily_n_inverse(center, r, n, theta, color='b'):
    # (n-2)/n个圆弧
    arc_degree_inverse(center, r, theta, theta+2*np.pi*(n-2)/n, color)

# 单层花


def lily_n(r, n, theta=0, color='b'):
    for i in range(0, n+1):
        onearc_lily_n((r*np.cos(i*2*np.pi/n+theta),
                       r*np.sin(i*2*np.pi/n+theta)), r, n, theta+(i+1)*2*np.pi/n, color)

# 单层花场


def lily_n_inverse(r, n, theta=0, color='b'):
    for i in range(0, n+1):
        onearc_lily_n_inverse((r*np.cos(i*2*np.pi/n+theta),
                               r*np.sin(i*2*np.pi/n+theta)), r, n, theta+(i+1)*2*np.pi/n, color)

# 花及场


def lily_with_feild(r, n, theta=0, color1='#00F', color2='#FF0'):
    lily_n_inverse(r, n, theta, color2)
    lily_n(r, n, theta, color1)

# m层，n瓣花

#

# 多层n瓣相似花


def lily_n_flower_similar(m, n, color='b'):
    if n % 2 == 1:
        for i in range(1, m+1):
            lily_n(np.sqrt(2*np.cos(np.pi/n))**i, n, -np.pi/2, color)
    else:
        for i in range(1, m+1):
            lily_n((2*(np.cos(np.pi/n)))**i, n, i*np.pi/n - np.pi/2, color)

# 多层n瓣花


def lily_n_flower(m, n, color='b'):
    if n % 2 == 1:
        for i in range(1, m+1):
            lily_n(np.sqrt(2*np.cos(np.pi/n))**i,
                   n, i*np.pi/n - np.pi/2, color)
    else:
        for i in range(1, m+1):
            lily_n((2*(np.cos(np.pi/n)))**i, n, i*np.pi/n, color)

# 多层n瓣相似花及场


def lily_n_flower_similar_with_feild(m, n, color1='#00F', color2='#FF0'):
    if n % 2 == 1:
        for i in range(1, m+1):
            lily_n_inverse(np.sqrt(2*np.cos(np.pi/n))**i, n, -np.pi/2, color2)
            lily_n(np.sqrt(2*np.cos(np.pi/n))**i, n, -np.pi/2, color1)
    else:
        for i in range(1, m+1):
            lily_n_inverse((2*(np.cos(np.pi/n)))**i, n,
                           i*np.pi/n - np.pi/2, color2)
            lily_n((2*(np.cos(np.pi/n)))**i, n, i*np.pi/n - np.pi/2, color1)

# 多层n瓣花及场


def lily_n_flower_with_feild(m, n,  color1='#00F', color2='#FF0'):
    if n % 2 == 1:
        for i in range(1, m+1):
            lily_n_inverse(np.sqrt(2*np.cos(np.pi/n))**i,
                           n, i*np.pi/n - np.pi/2, color2)
            lily_n(np.sqrt(2*np.cos(np.pi/n))**i,
                   n, i*np.pi/n - np.pi/2, color1)
    else:
        for i in range(1, m+1):
            lily_n_inverse((2*(np.cos(np.pi/n)))**i, n, i*np.pi/n, color2)
            lily_n((2*(np.cos(np.pi/n)))**i, n, i*np.pi/n, color1)

# 一朵花瓣朝向X轴


def n_lily_petal(center, r, n, theta, color='b'):
    alpha = np.pi/n
    beta = np.pi-np.pi/n
    center1 = (np.cos(theta+alpha)*r +
               center[0], np.sin(theta+alpha)*r+center[1])
    center2 = (np.cos(theta+alpha-2*np.pi/n)*r +
               center[0], np.sin(theta+alpha-2*np.pi/n)*r+center[1])
    # 圆心
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')
    arc_degree(center1, r, alpha+np.pi+theta,
               alpha+np.pi+theta+np.pi*(n-2)/n, color)
    arc_degree_inverse(center2, r, beta+theta,
                       beta+theta+np.pi*(n+2)/n, color)

# 一朵花瓣朝向X轴的场


def n_lily_petal_field(center, r, n, theta, color='b'):
    alpha = np.pi/n
    beta = np.pi-np.pi/n
    center1 = (np.cos(theta+alpha)*r +
               center[0], np.sin(theta+alpha)*r+center[1])
    center2 = (np.cos(theta+alpha-2*np.pi/n)*r +
               center[0], np.sin(theta+alpha-2*np.pi/n)*r+center[1])
    # 圆心
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')
    arc_degree_inverse(center1, r, alpha+np.pi+theta,
                       alpha+np.pi+theta+np.pi*(n-2)/n, color)
    arc_degree(center2, r, beta+theta,
               beta+theta+np.pi*(n+2)/n, color)

# 一朵向上花瓣


def one_petal(center, r, n, theta, color='b'):
    n_lily_petal(center, r, n, theta+np.pi/2, color)

# 一朵向上花瓣场


def one_petal_field(center, r, n, theta, color='b'):
    n_lily_petal_field(center, r, n, theta+np.pi/2, color)


# 花瓣形成的花
def flower_by_petal(center, r, M, N, n, theta, color='b'):
    for j in range(1, M+1):
        for i in range(0, N):
            one_petal(center, (np.sqrt(2*np.cos(np.pi/n))**(2*j-1)*r),
                      n, 2*i*np.pi/N+(j-1)*np.pi/N+theta, color)


def one_layer_flower_by_petal(center, R, n, theta, color):
    for i in range(0, n):
        one_petal(center, R, n, 2 * i * np.pi / n + theta, color)

# flower_by_petal((0, 0), 1, 3, 3, 5, 0, 'b')
# plt.show()


# lily_n(1, 8, 0)
# lily_with_feild(1, 4, 0)

# lily_n_flower(4, 9)
# lily_n_flower_similar(3, 9)

# lily_n_flower_with_feild(4, 9)
# lily_n_flower_similar_with_feild(4, s9)


# n_lily_petal((0, 0), 1, 2, 0)
# n_lily_petal((0, 0), 1, 3, 0)
# n_lily_petal((0, 0), 1, 4, 0)
# n_lily_petal((0, 0), 1, 5, 0, 'r')
# n_lily_petal((0, 0), 1, 7, 0, 'y')

# # n_lily_petal_field((0, 0), 1, 2, 0, 'g')
# n_lily_petal_field((0, 0), 1, 3, 0, 'g')
# n_lily_petal_field((0, 0), 1, 4, 0, 'g')
# n_lily_petal_field((0, 0), 1, 5, 0, 'g')
# n_lily_petal_field((0, 0), 1, 7, 0, 'g')
# for i in range(1, 200):
#     n_lily_petal((0, 0), 1, i, 0)
# plt.plot([0, 0], [-2, 2], 'b')
# plt.plot([-2, 2], [0, 0],  'b')
# one_petal((0, 0), 1, 3, 0)
# one_petal((1, 0), 1, 4, 0)
# one_petal_field((1, 0), 1, 4, 0)
# one_petal((1, 0), 1, 5, np.pi/2)
# one_petal((0, 0), 1, 6, 0, 'g')
# for i in range(3, 36):
#     one_petal((0, 0), 1, i, np.pi/2, 'g')
# arc_degree((0, 0), 2, 3*np.pi/2,
#            3*np.pi, 'b')

# arc_degree_inverse((0, 0), 2, 0,
#                    np.pi, 'b')

# for i in range(7, 10):
#     one_petal((0, 0), 1, i, 0, 'g')
# for i in range(3, 12):
#     one_petal((0, 0), 1, i, 0, 'b')
#     one_petal_field((0, 0), 1, i, 0, 'g')
# n = 4
# for i in range(0, 12):
#     one_petal((0, 0), 1, n, i*np.pi/6, 'g')
#     one_petal((0, 0), np.sqrt(2*np.cos(np.pi/n))
#               ** 2, n, i*np.pi/6+np.pi/12, 'g')
#     one_petal((0, 0), np.sqrt(2*np.cos(np.pi/4))
#               ** np.sqrt(9), n, i*np.pi/6, 'g')
# plt.show()
