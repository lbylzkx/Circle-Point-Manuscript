from circle import *
from arc import *
from arc_fill import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')

# 花瓣


def n_mandala_petal(center, R, r, n, theta=0, color='b'):
    alpha = 2*np.pi/n
    a = R*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    theta_arc = np.pi/2-np.pi/n+np.arccos((a)/r)
    theta_petal = 2*theta_arc
    # circle((0, 0), R, 'g')
    # circle((0, 0), R/2, 'g')
    center1 = (np.cos(theta+alpha/2)*R +
               center[0], np.sin(theta+alpha/2)*R+center[1])
    center2 = (np.cos(theta+alpha/2-2*np.pi/n)*R +
               center[0], np.sin(theta+alpha/2-2*np.pi/n)*R+center[1])
    if abs(r - a) < 1e-12:
        arc_degree(center1, r, np.pi+alpha/2+theta,
                   np.pi+alpha/2+theta+theta_arc, color)
        arc_degree(center2, r, np.pi/2+theta,
                   np.pi/2+theta+theta_arc, color)
        # if r == R:
        #     print("r=", r, ",a=", a)
        #     print('r=a,r=R形成睡莲花瓣。')
        # elif r > R:
        #     print("r=", r, ",a=", a)
        #     print('r=a,r>R形成荷花花瓣。')
        # elif r < R:
        #     print("r=", r, ",a=", a)
        #     print('r=a,r<R形成特殊曼陀罗花瓣。')
    elif r > a:
        arc_degree(center1, r, np.pi+alpha/2+theta,
                   np.pi+alpha/2+theta+theta_arc, color)
        arc_degree(center2, r, np.pi/2-beta+theta,
                   np.pi/2-beta+theta+theta_arc, color)
        # if r == R:
        #     print("r=", r, ",a=", a)
        #     print('r>a,r=R形成睡莲花瓣。')
        # elif r > R:
        #     print("r=", r, ",a=", a)
        #     print('r>a,r>R形成荷花花瓣。')
        # elif r < R:
        #     print("r=", r, ",a=", a)
        #     print('r>a,r<R形成普通曼陀罗花瓣。')
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')

# 花弧


def n_mandala_arc(center, R, r, n, theta=0, color='b'):
    alpha = 2*np.pi/n
    a = R*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    theta_arc = np.pi/2-np.pi/n+np.arccos((a)/r)
    theta_petal = 2*theta_arc
    # circle((0, 0), R, 'g')
    # circle((0, 0), R/2, 'g')
    center1 = (np.cos(theta+alpha/2)*R +
               center[0], np.sin(theta+alpha/2)*R+center[1])
    center2 = (np.cos(theta+alpha/2-2*np.pi/n)*R +
               center[0], np.sin(theta+alpha/2-2*np.pi/n)*R+center[1])
    if abs(r - a) < 1e-12:
        arc_degree(center1, r, np.pi/2+alpha+theta,
                   np.pi/2+alpha+theta+theta_petal, color)
        arc_degree(center2, r, np.pi/2+theta,
                   np.pi/2+theta+theta_petal, color)
        if r == R:
            print("r=", r, ",a=", a)
            print('r=a,r=R形成睡莲花弧。')
        elif r > R:
            print("r=", r, ",a=", a)
            print('r=a,r>R形成荷花花弧。')
        elif r < R:
            print("r=", r, ",a=", a)
            print('r=a,r<R形成特殊曼陀罗花弧。')
    elif r > a:
        arc_degree(center1, r, np.pi/2+alpha-beta+theta,
                   np.pi/2+alpha-beta+theta+theta_petal, color)
        arc_degree(center2, r, np.pi/2-beta+theta,
                   np.pi/2-beta+theta+theta_petal, color)
        if r == R:
            print("r=", r, ",a=", a)
            print('r>a,r=R形成睡莲花弧。')
        elif r > R:
            print("r=", r, ",a=", a)
            print('r>a,r>R形成荷花花弧。')
        elif r < R:
            print("r=", r, ",a=", a)
            print('r>a,r<R形成普通曼陀罗花弧。')
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')

# 带场花弧


def n_mandala_arc_with_field(center, R, r, n, theta=0, color='b', colorfield='#ff0'):
    alpha = 2*np.pi/n
    a = R*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    theta_arc = np.pi/2-np.pi/n+np.arccos((a)/r)
    theta_petal = 2*theta_arc
    # circle((0, 0), R, 'g')
    # circle((0, 0), R/2, 'g')
    center1 = (np.cos(theta+alpha/2)*R +
               center[0], np.sin(theta+alpha/2)*R+center[1])
    center2 = (np.cos(theta+alpha/2-2*np.pi/n)*R +
               center[0], np.sin(theta+alpha/2-2*np.pi/n)*R+center[1])
    if abs(r - a) < 1e-12:
        arc_degree(center1, r, np.pi/2+alpha+theta,
                   np.pi/2+alpha+theta+theta_petal, color)
        arc_degree_inverse(center1, r, np.pi/2+alpha+theta,
                           np.pi/2+alpha+theta+theta_petal, colorfield)
        arc_degree(center2, r, np.pi/2+theta,
                   np.pi/2+theta+theta_petal, color)
        arc_degree_inverse(center2, r, np.pi/2+theta,
                           np.pi/2+theta+theta_petal, colorfield)
    elif r > a:
        arc_degree(center1, r, np.pi/2+alpha-beta+theta,
                   np.pi/2+alpha-beta+theta+theta_petal, color)
        arc_degree_inverse(center1, r, np.pi/2+alpha-beta+theta,
                           np.pi/2+alpha-beta+theta+theta_petal, colorfield)
        arc_degree(center2, r, np.pi/2-beta+theta,
                   np.pi/2-beta+theta+theta_petal, color)
        arc_degree_inverse(center2, r, np.pi/2-beta+theta,
                           np.pi/2-beta+theta+theta_petal, colorfield)
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(center1[0], center1[1], marker='o', color='r')
    # plt.plot(center2[0], center2[1], marker='o', color='b')

# 一朵向上花瓣


def one_mandala_petal(center, R, r, n, theta=0, color='b'):
    n_mandala_petal(center, R, r, n, theta+np.pi/2, color)

# 一朵向上花瓣带填充


def one_mandala_petal_fill(center, R, r, n, theta=0, colorf='r', color='b', alpha=0.5):
    n_mandala_petal_fill(center, R, r, n, theta+np.pi/2, colorf, color, alpha)

# 一朵向上花弧


def one_mandala_arc(center, R, r, n, theta=0, color='b'):
    n_mandala_arc(center, R, r, n, theta+np.pi/2, color)

# 一朵向上花瓣场


def one_mandala_arc_with_field(center, R, r, n, theta=0, color='b', colorfield='#ff0'):
    n_mandala_arc_with_field(center, R, r, n, theta +
                             np.pi/2, color, colorfield)

# 花瓣形成的单层花


def mandala_flower_by_petal(center, R, r, N, n, theta, color='b'):
    for i in range(0, N):
        one_mandala_petal(center, R, r, n, 2*i*np.pi/N+theta, color)


def mandala_flower_by_petal_fill(center, R, r, N, n, theta, colorf='r', color='b', alpha=0.5):
    for i in range(0, N):
        one_mandala_petal_fill(center, R, r, n, 2*i *
                               np.pi/N+theta, colorf, color, alpha)

# 花弧形成的单层花


def mandala_flower_by_arc(center, R, r, N, n, theta, color='b'):
    for i in range(0, N):
        one_mandala_arc(center, R, r, n, 2*i*np.pi/N+theta, color)

# 单层花带场


def mandala_flower_by_arc_with_field(center, R, r, N, n, theta, color='b', colorfield='#ff0'):
    for i in range(0, N):
        one_mandala_arc_with_field(center, R, r, n, 2*i*np.pi/N+theta, color)


# 花瓣形成的多层花
def mandala_flower_by_petal_multi(center, R, r, n, ratio, M, N, theta, color='b'):
    for j in range(1, M+1):
        for i in range(0, N):
            one_mandala_petal(center, R*(ratio**(j-1)), r*(ratio**(j-1)),
                              n, 2*i*np.pi/N+(j-1)*np.pi/N+theta, color)


# n_mandala_petal((0, 0), 1, 0.7, 6, 0, color='b')
# n_mandala_arc((0, 0), 1, 0.7, 6, 0, color='b')
# n_mandala_arc_with_field((0, 0), 1, 0.7, 6, 0, color='b')
# n_mandala_petal((0, 0), 1, np.sin(np.pi/6), 6, 0, color='b')
# n_mandala_arc_with_field((0, 0), 1, np.sin(np.pi/6), 6, 0, color='b')
# n_mandala_arc((0, 0), 1, np.sin(np.pi/6), 6, 0, color='b')
# one_mandala_petal((0, 0), 1, 0.5, 6, 0, color='b')
# mandala_flower_by_petal((0, 0), 1, 0.5, 3, 3, 0, color='b')
# mandala_flower_by_petal((0, 0), 1, 1, 12, 4, 0, color='b')
# mandala_flower_by_arc_with_field((0, 0), 1, 1, 12, 4, 0, color='b')
# mandala_flower_by_petal((0, 0), np.sqrt(2), np.sqrt(2),
#                         12, 4, np.pi/12, color='b')
# mandala_flower_by_petal((0, 0), 1, 2, 12, 6, 0, color='b')
# mandala_flower_by_petal((0, 0), 1, 2, 12, 4, 0, color='r')
# mandala_flower_by_petal((0, 0), 1, 2, 12, 3, 0, color='g')
# mandala_flower_by_petal((0, 0), 1, 2, 12, 5, 0, color='purple')
# mandala_flower_by_petal((0, 0), 1, 2, 72, 144, 0, color='cyan')
# mandala_flower_by_petal((0, 0), 1, 2, 72, 3, 0, color='y')
# mandala_flower_by_petal_fill(
#     (0, 0), 1, 0.6, 24, 6, 0, color='b', colorf='r', alpha=0.5)

# mandala_flower_by_petal_multi(
#     (0, 0), 1, 2, 4, np.sqrt(3), 3, 12, 0, color='#f00')
# mandala_flower_by_petal_multi(
#     (0, 0), 1, 1, 4, np.sqrt(3), 3, 12, 0, color='#0f0')
# mandala_flower_by_petal_multi(
#     (0, 0), 1, 0.8, 4, np.sqrt(3), 3, 12, 0, color='b')


# mandala_flower_by_petal_multi(
#     (0, 0), 1, 1, 6, np.sqrt(3), 2, 6, 0, color='#0f0')
# mandala_flower_by_petal_multi(
#     (0, 0), 1, 1, 6, np.sqrt(3), 2, 6, np.pi/6, color='#0f0')
# plt.axis('equal')
# plt.show()
