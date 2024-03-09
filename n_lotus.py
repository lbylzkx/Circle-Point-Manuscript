from circle import *
from arc import *
# from rodincoil import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def n_lotus_petal(center, R, r, n, theta=0, color='b'):
    alpha = np.pi/n
    alpha1 = np.arccos((R/r)*np.sin(np.pi/n))
    theta_arc = 2*alpha1
    # circle((0, 0), R, 'g')
    center1 = (np.cos(theta+alpha)*R +
               center[0], np.sin(theta+alpha)*R+center[1])
    center2 = (np.cos(theta+alpha-2*np.pi/n)*R +
               center[0], np.sin(theta+alpha-2*np.pi/n)*R+center[1])
    arc_degree(center1, r, np.pi+(np.pi/2-alpha1)+theta,
               np.pi+(np.pi/2-alpha1)+theta+theta_arc, color)
    arc_degree(center2, r, (np.pi/2-alpha1)+theta,
               (np.pi/2-alpha1)+theta+theta_arc, color)
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')


def one_lotus_petal(center, R, r, n, theta=0, color='b'):
    n_lotus_petal(center, R, r, n, theta+np.pi/2, color)


def lotus_flower_by_petal(center, R, r, N, n, theta, color='b'):
    # for j in range(1, M+1):
    for i in range(0, N):
        one_lotus_petal(center, R, r, n, 2*i*np.pi/N+theta, color)


def lotus_flower_by_petal_colorful(center, R, r, N, n, theta, colors):
    # for j in range(1, M+1):
    for i in range(0, N):
        one_lotus_petal(center, R, r, n, 2*i*np.pi/N+theta, colors[i])
# lotus_flower_by_petal((0, 0), 1, 2, 12, 12, 0, '#0f0')

# # one_lotus_petal((0, 0), 1, 2, 6, 0, 'r')
# # n_lotus_petal((0, 0),  1, 2, 6, 0, 'r')
# plt.axis('equal')
# plt.show()
