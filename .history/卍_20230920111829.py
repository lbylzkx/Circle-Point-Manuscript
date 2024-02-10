import numpy as np
import matplotlib.pyplot as plt


def x_position(n, thelta=0):
    return np.sqrt(2)**n*np.cos(n*np.pi/4+thelta)


def y_position(n, thelta=0):
    return np.sqrt(2)**n*np.sin(n*np.pi/4+thelta)

axis_x = [x_position(10), x_position(10,thelta=np.pi)]
axis_y = [y_position(10)]

plt.plot()
x1 = [x_position(i, thelta=0) for i in range(-10, 10)]
y1 = [y_position(i, thelta=0) for i in range(-10, 10)]
plt.plot(x1, y1)

x2 = [x_position(i, thelta=np.pi/2) for i in range(-10, 10)]
y2 = [y_position(i, thelta=np.pi/2) for i in range(-10, 10)]
plt.plot(x2, y2)

x3 = [x_position(i, thelta=np.pi) for i in range(-10, 10)]
y3 = [y_position(i, thelta=np.pi) for i in range(-10, 10)]
plt.plot(x3, y3)

x4 = [x_position(i, thelta=3*np.pi/2) for i in range(-10, 10)]
y4 = [y_position(i, thelta=3*np.pi/2) for i in range(-10, 10)]
plt.plot(x4, y4)

plt.axis('equal')
plt.show()
