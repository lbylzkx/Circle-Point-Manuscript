import numpy as np
import matplotlib.pyplot as plt
from circle import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


# 9:(-1,1);10:(1,1);11:(0,3/2);12:(0,2),
# 5:(0,-1/2);6:(-1,0);7:(1,0);8:(0,1/2);
# 1:(0,-2);2:(0,-3/2);3:(-1,-1);4:(1,-1);
# ConcentricCircles()
def Kathara(n, color='b'):
    ConcentricCircles((0, 2), n, 1, color)
    ConcentricCircles((0, 3/2), n, 1, color)
    ConcentricCircles((1, 1), n, 1, color)
    ConcentricCircles((-1, 1), n, 1, color)
    ConcentricCircles((0, 1/2), n, 1, color)
    ConcentricCircles((1, 0), n, 1, color)
    ConcentricCircles((-1, 0), n, 1, color)
    ConcentricCircles((0, -1/2), n, 1, color)
    ConcentricCircles((1, -1), n, 1, color)
    ConcentricCircles((-1, -1), n, 1, color)
    ConcentricCircles((0, -3/2), n, 1, color)
    ConcentricCircles((0, -2), n, 1, color)


def Kathara_Pro(n, q, color='b'):
    ConcentricCircles_Pro((0, 2), n, q, 1, color)
    ConcentricCircles_Pro((0, 3/2), n, q, 1, color)
    ConcentricCircles_Pro((1, 1), n, q, 1, color)
    ConcentricCircles_Pro((-1, 1), n, q, 1, color)
    ConcentricCircles_Pro((0, 1/2), n, q, 1, color)
    ConcentricCircles_Pro((1, 0), n, q, 1, color)
    ConcentricCircles_Pro((-1, 0), n, q, 1, color)
    ConcentricCircles_Pro((0, -1/2), n, q, 1, color)
    ConcentricCircles_Pro((1, -1), n, q, 1,  color)
    ConcentricCircles_Pro((-1, -1), n, q, 1,  color)
    ConcentricCircles_Pro((0, -3/2), n, q, 1,  color)
    ConcentricCircles_Pro((0, -2), n, q, 1, color)


def Kathara_C(n):
    ConcentricCircles((0, 2), n, 1, '#FFF')
    ConcentricCircles((0, 3/2), n, 1, 'grey')
    ConcentricCircles((1, 1), n, 1, '#0000FF')
    ConcentricCircles((-1, 1), n, 1, '#C0C0C0')
    ConcentricCircles((0, 1/2), n, 1, 'gold')
    ConcentricCircles((1, 0), n, 1, 'violet')
    ConcentricCircles((-1, 0), n, 1, 'indigo')
    ConcentricCircles((0, -1/2), n, 1, 'blue')
    ConcentricCircles((1, -1), n, 1, 'g')
    ConcentricCircles((-1, -1), n, 1, 'y')
    ConcentricCircles((0, -3/2), n, 1, 'orange')
    ConcentricCircles((0, -2), n, 1, 'r')


def Kathara_Pro_C(n, q):
    ConcentricCircles_Pro((0, 2), n, q, 1, 'white')
    ConcentricCircles_Pro((0, 3/2), n, q, 1, 'grey')
    ConcentricCircles_Pro((1, 1), n, q, 1, '#00F')
    ConcentricCircles_Pro((-1, 1), n, q, 1, '#C0C0C0')
    ConcentricCircles_Pro((0, 1/2), n, q, 1, 'gold')
    ConcentricCircles_Pro((1, 0), n, q, 1, 'violet')
    ConcentricCircles_Pro((-1, 0), n, q, 1, 'indigo')
    ConcentricCircles_Pro((0, -1/2), n, q, 1, 'blue')
    ConcentricCircles_Pro((1, -1), n, q, 1,  'g')
    ConcentricCircles_Pro((-1, -1), n, q, 1,  'y')
    ConcentricCircles_Pro((0, -3/2), n, q, 1,  'orange')
    ConcentricCircles_Pro((0, -2), n, q, 1, 'r')


# plt.figure(facecolor='black')
# Kathara(2, 'g')
# Kathara_Pro(2, np.sqrt(2), 'g')
# Kathara_Pro_C(2, np.sqrt(2), 'c')

# plt.axis('equal')
# plt.axis('off')
# plt.show()
