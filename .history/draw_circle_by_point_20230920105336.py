import matplotlib.pyplot as plt
import numpy as np


def circle(center, radius, color='b'):
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


# 给定点的坐标
center = (1, 1)
# 圆周上一点的坐标
point = (2, 3)

# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Circle')
# plt.grid(True)
plt.show()
