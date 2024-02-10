import numpy as np
import matplotlib.pyplot as plt


def circle(center, radius):
    x = center[0] + radius * np.cos(2*np.pi)
    y = center[1] + radius * np.sin(2*np.pi)
    plt.plot(x, y)


plt.gca().set_aspect('equal', adjustable='box')
plt.show()
