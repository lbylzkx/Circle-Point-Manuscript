import numpy as np
import matplotlib.pyplot as plt


def circle(center, radius):
    angle = np.linspace(0, 2*np.pi, 1000)
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    plt.axis('equal')
    plt.plot(x, y)


circle((0, 0), 2)

plt.show()
