
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def logSpiral(n, a, b, cyc, color='b', theta=0):
    t = np.linspace(-cyc * 2 * np.pi, cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+theta)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+theta)
    plt.plot(x, y, color)
    # plt.axis('equal')


def logSpiral_out(n, a, b, cyc, color='b', theta=0):
    t = np.linspace(0, cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+theta)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+theta)
    plt.plot(x, y, color)


def logSpiral_in(n, a, b, cyc, color='b', theta=0):
    t = np.linspace(0, -cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+theta)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+theta)
    plt.plot(x, y, color)


def n_spiral(n, cyc, color, theta=0):
    for i in range(n):
        logSpiral(n, 1, 1, cyc, color, theta+i*2*np.pi/n)
        logSpiral(n, -1, 1, cyc, color, theta+i*2*np.pi/n)


def n_spiral_rotate(n, cyc, color, alpha=0, theta=0):
    for i in range(n):
        logSpiral(n, 1, 1, cyc, color, alpha+theta+i*2*np.pi/n)
        logSpiral(n, -1, 1, cyc, color, alpha-theta+i*2*np.pi/n)


def n_spiral_rotate_out(n, cyc, color, theta=0):
    for i in range(n):
        logSpiral_out(n, 1, 1, cyc, color, theta+i*2*np.pi/n)
        logSpiral_out(n, -1, 1, cyc, color, -theta+i*2*np.pi/n)


def n_spiral_rotate_in(n, cyc, color, theta=0):
    for i in range(n):
        logSpiral_in(n, 1, 1, cyc, color, theta+i*2*np.pi/n)
        logSpiral_in(n, -1, 1, cyc, color, -theta+i*2*np.pi/n)


def calla_petal(n, cyc, theta, color):
    logSpiral(n, 1, 1, cyc*1.25, color, theta)
    logSpiral(n, -1, 1, cyc*1.25, color, -theta)


def calla_by_petal(n, cyc, N, theta, colors):
    for i in range(N):
        calla_petal(n, cyc, theta+i*2*np.pi/N, colors[i])


# n_spiral(9, -1, 'g', 0)


# n_spiral(8, 1, 'r', 0)
# n_spiral_r(4, 1, 'g', np.pi/9)
# n_spiral(7, 1.5, 'g', np.pi/14)
# plt.axis('equal')
# plt.show()
