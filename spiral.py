
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def logSpiral(n, a, b, cyc, color='b', theta=0):
    t = np.linspace(0, cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+theta)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+theta)
    plt.plot(x, y, color)
    # plt.axis('equal')


def n_spiral(n, cyc, color, theta=0):
    for i in range(n):
        logSpiral(n, 1, 1, cyc, color, theta+i*2*np.pi/n)
        logSpiral(n, -1, 1, cyc, color, theta+i*2*np.pi/n)


def n_spiral_rotate(n, cyc, color, theta=0):
    for i in range(n):
        logSpiral(n, 1, 1, cyc, color, theta+i*2*np.pi/n)
        logSpiral(n, -1, 1, cyc, color, -theta+i*2*np.pi/n)

# n_spiral(9, -1, 'g', 0)


# n_spiral(8, 1, 'r', 0)
# n_spiral_r(4, 1, 'g', np.pi/9)
# n_spiral(7, 1.5, 'g', np.pi/14)
# plt.axis('equal')
# plt.show()
