import matplotlib.pyplot as plt
import numpy as np

# 给定点的坐标
center = (1, 1)
# 圆周上一点的坐标
point_on_circle = (2, 3)

# 计算圆的半径
radius = np.sqrt((point_on_circle[0] - center[0])
                 ** 2 + (point_on_circle[1] - center[1]) ** 2)

# 生成圆上的点
theta = np.linspace(0, 2 * np.pi, 100)
x = center[0] + radius * np.cos(theta)
y = center[1] + radius * np.sin(theta)

# 绘制图形
plt.plot(x, y)
# plt.axis('equal')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Circle')
# plt.grid(True)
plt.show()
