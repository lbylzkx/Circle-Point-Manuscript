
import numpy as np
import matplotlib.pyplot as plt
n = 4


def logSpiral(n, a, b, cyc, theta=0):
    t = np.linspace(0, cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+theta)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+theta)
    plt.plot(x, y)
    plt.axis('equal')


def n_spiral(n, cyc, theta=0):
    for i in range(n):
        n_spiral(n, 1, 1, cyc, theta+i*2*np.pi/n)
        n_spiral(n, -1, 1, cyc, theta+i*2*np.pi/n)


n_spiral(n, 1, 1, 1, 2*np.pi/n)
# n_spiral(9, 3, 0)

plt.show()
