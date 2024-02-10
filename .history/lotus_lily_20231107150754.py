import numpy as np
import matplotlib.pyplot as plt
from arc import *
from lotus import *
from waterlily import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

# 正旋
# clockwise
for alpha in range(0, 12):
    for n in range(-10, 9):
        arc((loutus_x_center(n, alpha*np.pi/6), loutus_y_center(n, alpha*np.pi/6)),
            (loutus_x_from(n, alpha*np.pi/6), loutus_y_from(n, alpha*np.pi/6)),
            (loutus_x_to(n, alpha*np.pi/6), loutus_y_to(n, alpha*np.pi/6)), 'r')
