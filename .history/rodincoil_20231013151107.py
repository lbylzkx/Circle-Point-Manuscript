import numpy as np
import matplotlib.pyplot as plt
from circle import *

R = 1
r = 2*R
for n in range(0, 12):
    circle((R*np.cos(n*np.pi/6), R*np.sin(n*np.pi/6)), r)
plt.axis('equal')
plt.show()
