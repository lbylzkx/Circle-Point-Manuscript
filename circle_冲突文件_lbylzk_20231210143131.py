import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def circle(center, radius, color='b'):
    angle = np.linspace(0, 2*np.pi, 1000)
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    plt.axis('equal')
    plt.plot(x, y, color)


def circle_p(center, point, color='b'):
    # 计算圆的半径
    radius = np.sqrt((point[0] - center[0])
                     ** 2 + (point[1] - center[1]) ** 2)
    # 生成圆上的点
    theta = np.linspace(0, 2 * np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)
    # 绘制图形
    plt.axis('equal')
    plt.plot(x, y, color)


def ConcentricCircles(center, n, radius, color='b'):
    plt.plot(center[0], center[1],marker='o', color)
    circle(center, radius, color)
    for i in range(n):
        circle(center, radius-i, color)
        circle(center, radius+i, color)


ConcentricCircles((0, 0), 10, 1, 'g')
plt.show()
