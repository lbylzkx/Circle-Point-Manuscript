# import matplotlib.pyplot as plt
# import numpy as np

# N = 5
import numpy as np
import matplotlib.pyplot as plt
R = 10
# points = [[R*np.cos(i*2 * np.pi/N), R*np.sin(i*2 * np.pi/N)] for i in range(N)]

# for i in range(-1, len(points) - 1):
#     plt.plot([points[i][0], points[i+1][0]],
#              [points[i][1], points[i+1][1]], color='r')
#     # 连接两个点
#     plt.scatter([points[i][0], points[i+1][0]],
#                 [points[i][1], points[i+1][1]], color='b')
#     # 绘制点
# plt.axis('equal')
# plt.show()

N = 100
points = [[np.cos(i*2 * np.pi/N), np.sin(i*2 * np.pi/N)] for i in range(N)]

for i in range(len(points)):
    for j in range(i+1, len(points)):
        plt.plot([points[i][0], points[j][0]],
                 [points[i][1], points[j][1]], color='r')
    plt.scatter(points[i][0], points[i][1], color='b')

plt.axis('equal')
plt.show()
