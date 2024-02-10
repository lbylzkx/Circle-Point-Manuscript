import numpy as np
import matplotlib.pyplot as plt


def circle(center, radius, angle):
    x = center[0] + radius * np.cos(np.deg2rad(angle))
    y = center[1] + radius * np.sin(np.deg2rad(angle))
    return x, y
