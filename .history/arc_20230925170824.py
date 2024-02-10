import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

""""""
# 从point1到point2的圆弧
""""""

# 顺时针


def arc(center, point1, point2, color='b'):
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

    # X,Y轴等长
    plt.axis('equal')
    # 绘制圆弧
    plt.plot(x, y, color)

# 逆时针


def arc_inverse(center, point1, point2, color='b'):
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

    # X,Y轴等长
    plt.axis('equal')
    # 绘制圆弧
    plt.plot(x, y, color)


# 示例
# arc((1, 1), (2, 1), (1, 0), 'r')
# arc((1, 1), (1, 0), (2, 1), 'r')
# arc_inverse((1, 1), (1, 0), (2, 1), 'g')
# plt.axis('equal')
# plt.show()
