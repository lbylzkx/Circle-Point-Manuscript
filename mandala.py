
from circle import *
from arc import *
from arc_fill import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


def n_mandala_petal(center, R, r, n, theta=0, color='b'):
    alpha = np.pi/n
    alpha1 = np.pi/2-np.pi/n+np.arccos((R*np.sin(np.pi/n))/r)
    theta_arc = 2*alpha1
    beta = np.pi-2*np.pi/n-alpha1
    circle((0, 0), R, 'g')
    circle((0, 0), R/2, 'g')
    center1 = (np.cos(theta+alpha)*R +
               center[0], np.sin(theta+alpha)*R+center[1])
    center2 = (np.cos(theta+alpha-2*np.pi/n)*R +
               center[0], np.sin(theta+alpha-2*np.pi/n)*R+center[1])
    if r > R/2:
        arc_degree(center1, r, np.pi/2+beta+theta,
                   np.pi/2+beta+theta+theta_arc, color)
        arc_degree(center2, r, alpha+beta+theta,
                   alpha+beta+theta+theta_arc, color)
    else:
        arc_degree(center1, r, (np.pi/2+alpha1)+theta,
                   (np.pi/2+alpha1)+theta+theta_arc, color)
        arc_degree(center2, r, (alpha1)+alpha+theta,
                   (alpha1)+alpha+theta+theta_arc, color)
    plt.plot(center1[0], center1[1], marker='o', color='r')
    plt.plot(center2[0], center2[1], marker='o', color='b')


def one_mandala_petal(center, R, r, n, theta=0, color='b'):
    n_mandala_petal(center, R, r, n, theta+np.pi/2, color)


def mandala_flower_by_petal(center, R, r, N, n, theta, color='b'):
    for i in range(0, N):
        one_mandala_petal(center, R, r, n, 2*i*np.pi/N+theta, color)


n_mandala_petal((0, 0), 1, 0.5, 7, 0, color='b')
# one_mandala_petal((0, 0), 1, 0.5, 6, 0, color='b')
# mandala_flower_by_petal((0, 0), 1, 0.6, 7, 7, 0, color='b')
plt.axis('equal')
plt.show()
