import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def circle(center, radius, color='b'):
    angle = np.linspace(0, 2*np.pi, 1000)
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    plt.axis('equal')
    plt.plot(x, y, color)
