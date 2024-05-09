import matplotlib.pyplot as plt
import numpy as np
from arc import *
# from symmetric import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

# 顺时针


def arc_dot(center, point1, point2):
    # 计算端点到圆心的向量
    vector1 = np.array(point1) - np.array(center)
    vector2 = np.array(point2) - np.array(center)

    # 计算向量的模长
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # 计算向量之间的夹角
    theta1 = np.arctan2(vector1[1], vector1[0])
    theta2 = np.arctan2(vector2[1], vector2[0])

    # 确保 theta2 > theta1
    if theta1 < theta2:
        theta1 += 2 * np.pi

    # 计算圆弧上的点
    t = np.linspace(theta1, theta2, 100)
    x = center[0] + r1 * np.cos(t)
    y = center[1] + r1 * np.sin(t)

    return [x, y]

# 逆时针


def arc_inverse_dot(center, point1, point2):
    # 计算端点到圆心的向量
    vector1 = np.array(point1) - np.array(center)
    vector2 = np.array(point2) - np.array(center)

    # 计算向量的模长
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # 计算向量之间的夹角
    theta1 = np.arctan2(vector1[1], vector1[0])
    theta2 = np.arctan2(vector2[1], vector2[0])

    # 确保 theta2 > theta1
    if theta2 < theta1:
        theta2 += 2 * np.pi

    # 计算圆弧上的点
    t = np.linspace(theta1, theta2, 100)
    x = center[0] + r1 * np.cos(t)
    y = center[1] + r1 * np.sin(t)

    return [x, y]


"""通过角度画圆弧
"""


def arc_degree_p(center, radius, angle1, angle2, color):
    if angle1 < angle2:
        angle = np.linspace(angle1, angle2, 1000)
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
    return [x, y]


def arc_degree_p_inverse(center, radius, angle1, angle2, color):
    angle = np.linspace(angle2-2*np.pi, angle1, 1000)
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    return [x, y]


# def arc_contour(center, point1, point2, color='b'):
#     arc = arc_dot(center, point1, point2)
#     # arc_inverse = arc_inverse_dot(center, point1, point2)
#     sym = symmetric_point(point1, point2, arc)
#     # 使用 np.concatenate 函数来拼接两个圆弧的坐标
#     # x = np.concatenate((arc[0], sym[0][::-1]))
#     # y = np.concatenate((arc[1], sym[1][::-1]))
#     # X,Y轴等长
#     plt.axis('equal')
#     # 绘制圆弧
#     plt.plot(arc[0], arc[1], color)
#     plt.plot(sym[0], sym[1], color)


# def arc_fill(center, point1, point2, color='b'):
#     arc = arc_dot(center, point1, point2)
#     arc_inverse = arc_inverse_dot(center, point1, point2)
#     # 使用 np.concatenate 函数来拼接两个圆弧的坐标
#     x = np.concatenate((arc[0], arc_inverse[0][::-1]))
#     y = np.concatenate((arc[1], arc_inverse[1][::-1]))
#     # X,Y轴等长
#     plt.axis('equal')
#     # 绘制圆弧
#     plt.fill(x, y, color)


def onearc_lily_n(center, r, n, theta, color='b'):
    # (n-2)/n个圆弧
    arc_degree(center, r, theta, theta+2*np.pi*(n-2)/n, color)


def onearc_lily_n_inverse(center, r, n, theta, color='b'):
    # (n-2)/n个圆弧
    arc_degree_inverse(center, r, theta, theta+2*np.pi*(n-2)/n, color)


def n_lily_petal_fill(center, r, n, theta, colorf='b', color='r', alpha=0.1):
    alpha = np.pi/n
    beta = np.pi-np.pi/n
    center1 = (np.cos(theta+alpha)*r +
               center[0], np.sin(theta+alpha)*r+center[1])
    center2 = (np.cos(theta+alpha-2*np.pi/n)*r +
               center[0], np.sin(theta+alpha-2*np.pi/n)*r+center[1])
    # 圆心
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')
    arc = arc_degree_p(center1, r, alpha+np.pi+theta,
                       alpha+np.pi+theta+np.pi*(n-2)/n, color)
    arc_inverse = arc_degree_p_inverse(center2, r, beta+theta,
                                       beta+theta+np.pi*(n+2)/n, color)
    x = arc[0]
    y = arc[1]
    x1 = arc_inverse[0]
    y1 = arc_inverse[1]
    # X,Y轴等长
    plt.axis('equal')
    plt.fill(x, y, colorf)
    plt.fill(x1, y1, colorf)
    plt.plot(x, y, color, alpha)
    plt.plot(x1, y1, color, alpha)


def n_mandala_petal_fill(center, R, r, n, theta=0, colorf='b', color='r', alpha=0.1):
    alpha = 2*np.pi/n
    a = R*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    theta_arc = np.pi/2-np.pi/n+np.arccos((a)/r)
    theta_petal = 2*theta_arc
    # circle((0, 0), R, 'g')
    # circle((0, 0), R/2, 'g')
    center1 = (np.cos(theta+alpha/2)*R +
               center[0], np.sin(theta+alpha/2)*R+center[1])
    center2 = (np.cos(theta+alpha/2-2*np.pi/n)*R +
               center[0], np.sin(theta+alpha/2-2*np.pi/n)*R+center[1])
    if abs(r - a) < 1e-12:
        arc = arc_degree_p(center1, r, np.pi+alpha/2+theta,
                           np.pi+alpha/2+theta+theta_arc, color)
        arc_inverse = arc_degree_p(center2, r, np.pi/2+theta,
                                   np.pi/2+theta+theta_arc, color)
    elif r > a:
        arc = arc_degree_p(center1, r, np.pi+alpha/2+theta,
                           np.pi+alpha/2+theta+theta_arc, color)
        arc_inverse = arc_degree_p(center2, r, np.pi/2-beta+theta,
                                   np.pi/2-beta+theta+theta_arc, color)
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')
    x1 = arc[0]
    y1 = arc[1]
    x2 = arc_inverse[0]
    y2 = arc_inverse[1]
    merged_x = np.concatenate((x1, x2))
    merged_y = np.concatenate((y1, y2))
    plt.axis('equal')

    plt.fill(merged_x, merged_y, colorf)
    # plt.fill(x1, y1, colorf)
    # plt.fill(x2, y2, colorf)
    plt.plot(x1, y1, color, alpha)
    plt.plot(x2, y2, color, alpha)


# arc_degree_fill((0, 0), 1, 0, np.pi/2, 'r')
# n_lily_petal_fill((0, 0), 1, 4, np.pi/2, 'b')
# arc_fill((1, 1), (1, 0), (0, 0), 'g')
# arc_contour((1, 1), (1, 0), (0, 0), 'r')
# # arc_dot((1, 1), (1, 0), (0, 0))
# arc_inverse_dot((1, 1), (1, 0), (0, 0))
# n_mandala_petal_fill((0, 0), 1, 2, 6, 0, '#f0f', '#0ff', 0.5)
# plt.show()
