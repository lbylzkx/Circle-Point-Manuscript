import numpy as np
import matplotlib.pyplot as plt


def circle(center, radius):
    x = center[0] + radius * np.cos(2*np.pi)
    y = center[1] + radius * np.sin(2*np.pi)
    plt.axis('equal')
    plt.plot(x, y)


circle((0, 0), 2)

plt.axis('equal')
plt.show()
