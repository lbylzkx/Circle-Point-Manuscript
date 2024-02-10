import matplotlib.pyplot as plt
import numpy as np

N = 5
points = [[np.cos(i*2 * np.pi/N), np.sin(i*2 * np.pi/N)] for i in range(N)]

for i in range(len(points) - 1):
    plt.plot([points[i][0], points[i+1][0]],
             [points[i][1], points[i+1][1]], color='r')
    # 连接两个点
    plt.scatter([points[i][0], points[i+1][0]],
                [points[i][1], points[i+1][1]], color='b')
    # 绘制点

plt.show()
