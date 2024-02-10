import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


class Draw_Arc:

    point1 = [0, 0]
    point2 = [0, 0]
    center = [0, 0]

    def __init__(self) -> None:
        point1 = [0, 0]
        point2 = [0, 0]
        center = [0, 0]

    """"""
    # 从point1到point2的圆弧
    """"""

# 顺时针

    def arc(self, center, point1, point2, color='b'):
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

    def arc_inverse(self, center, point1, point2, color='b'):
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

    """通过角度画圆弧
    """
# 角度画弧

    def arc_degree(self, center, radius, angle1, angle2, color='b'):
        angle = np.linspace(angle1, angle2, 1000)
        x = center[0] + radius * np.cos(angle)
        y = center[1] + radius * np.sin(angle)
        plt.axis('equal')
        plt.plot(x, y, color)


Draw_Arc.arc(0, (0, 1), (2, 1), (1, 2))
Draw_Arc.arc(0, (0, 1), (1, 2), (2, 1))
plt.show()
