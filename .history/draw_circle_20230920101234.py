import numpy as np
import matplotlib.pyplot as plt


def arc(center, radius, angle):
    x = center[0] + radius * np.cos(np.deg2rad(angle))
    y = center[1] + radius * np.sin(np.deg2rad(angle))
    return x, y


center = (0, 0)
radius = 1
angle = np.linspace(0, 360, 100)
x, y = arc(center, radius, angle)

plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
