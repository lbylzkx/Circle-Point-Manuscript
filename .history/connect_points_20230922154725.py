import matplotlib.pyplot as plt
import numpy as np

points = [[x,y] in [np.cos(i*2 * np.pi/5),np.sin(i*2 * np.pi/5) for i in range(5)]]
for i in range(len(points) - 1):
    plt.plot([points[i][0], points[i+1][0]],
             [points[i][1], points[i+1][1]], color='r')
    # 连接两个点
    plt.scatter([points[i][0], points[i+1][0]],
                [points[i][1], points[i+1][1]], color='b')
    # 绘制点

plt.show()
