import numpy as np
import matplotlib.pyplot as plt


def x_position(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def y_position(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)


x = [x_position(i, thelta=0) for i in range(-10, 10)]
y = [y_position(i, thelta=0) for i in range(-10, 10)]

plt.plot(x, y, 'o')
plt.show()
