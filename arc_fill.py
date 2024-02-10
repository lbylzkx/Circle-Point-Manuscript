import matplotlib.pyplot as plt
import numpy as np
from symmetric import *
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


def arc_contour(center, point1, point2, color='b'):
    arc = arc_dot(center, point1, point2)
    # arc_inverse = arc_inverse_dot(center, point1, point2)
    sym = symmetric_point(point1, point2, arc)
    # 使用 np.concatenate 函数来拼接两个圆弧的坐标
    # x = np.concatenate((arc[0], sym[0][::-1]))
    # y = np.concatenate((arc[1], sym[1][::-1]))
    # X,Y轴等长
    plt.axis('equal')
    # 绘制圆弧
    plt.plot(arc[0], arc[1], color)
    plt.plot(sym[0], sym[1], color)


def arc_fill(center, point1, point2, color='b'):
    arc = arc_dot(center, point1, point2)
    arc_inverse = arc_inverse_dot(center, point1, point2)
    # 使用 np.concatenate 函数来拼接两个圆弧的坐标
    x = np.concatenate((arc[0], arc_inverse[0][::-1]))
    y = np.concatenate((arc[1], arc_inverse[1][::-1]))
    # X,Y轴等长
    plt.axis('equal')
    # 绘制圆弧
    plt.fill(x, y, color)


# arc_fill((1, 1), (1, 0), (0, 0), 'g')
# arc_contour((1, 1), (1, 0), (0, 0), 'r')
# # arc_dot((1, 1), (1, 0), (0, 0))
# # arc_inverse_dot((1, 1), (1, 0), (0, 0))
# plt.show()
