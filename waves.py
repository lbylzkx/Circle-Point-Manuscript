from circle import *
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


# fig, ax = plt.subplots(figsize=(9, 9))
# ax.set_aspect('equal')

# fig.patch.set_facecolor('black')

# A:振幅Amplitude
# F:频率Frequency
# P:相位Phase
# A = 3
# F = 3
# P = 12

# color = '#0F0'
colors = ['r', 'orange', 'yellow', 'green', 'blue', 'purple',
               'r', 'orange', 'yellow', 'green', 'blue', 'purple']*2
# 等差数列振幅
# 向外
# ConcentricCircles_o((0, 0), F, A, 1, 'g')
# for i in range(P+1):
#     ConcentricCircles_o((np.cos(i*2*np.pi/P+np.pi/2),
#                         np.sin(i*2*np.pi/P+np.pi/2)), F, A, 1, 'g')
# # # 向内
# ConcentricCircles_i((0, 0), F, A, 1, 'g')
# for i in range(P+1):
#     ConcentricCircles_i((np.cos(i*2*np.pi/P+np.pi/2),
#                         np.sin(i*2*np.pi/P+np.pi/2)), F, A, 1, 'g')
# # 双向
# ConcentricCircles((0, 0), F, A, 1, 'g')
# for i in range(P+1):
#     ConcentricCircles((np.cos(i*2*np.pi/P+np.pi/2),
#                        np.sin(i*2*np.pi/P+np.pi/2)), F, A, 1, 'g')

# # 等比数列振幅

# # 向外
# ConcentricCircles_Pro_o((0, 0), F, np.sqrt(A), 1, color)
# for i in range(P+1):
#     ConcentricCircles_Pro_o(
#         ((np.cos(i*2*np.pi/P+np.pi/2)), np.sin(i*2*np.pi/P+np.pi/2)), F, np.sqrt(A), 1, color)

# # 向内
# ConcentricCircles_Pro_i((0, 0), F, np.sqrt(A), 1, color)
# for i in range(P+1):
#     ConcentricCircles_Pro_i(
#         ((np.cos(i*2*np.pi/P+np.pi/2)), np.sin(i*2*np.pi/P+np.pi/2)), F, np.sqrt(A), 1, color)

# # 双向
# ConcentricCircles_Pro((0, 0), F, np.sqrt(A), 1, color)
# for i in range(P+1):
#     ConcentricCircles_Pro(
#         ((np.cos(i*2*np.pi/P+np.pi/2)), np.sin(i*2*np.pi/P+np.pi/2)), F, np.sqrt(A), 1, color)

# 圈上波

# 等差

# 向外


def wave_circle_ari_o(A, F, P, color, R=1):
    ConcentricCircles_o((0, 0), F, A, R, 'g')
    for i in range(P+1):
        ConcentricCircles_o((np.cos(i*2*np.pi/P+np.pi/2),
                            np.sin(i*2*np.pi/P+np.pi/2)), F, A, R, 'g')
# 向内


def wave_circle_ari_i(A, F, P, color, R=1):
    ConcentricCircles_i((0, 0), F, A, R, 'g')
    for i in range(P+1):
        ConcentricCircles_i((np.cos(i*2*np.pi/P+np.pi/2),
                            np.sin(i*2*np.pi/P+np.pi/2)), F, A, R, 'g')

# 双向


def wave_circle_ari(A, F, P, color, R=1):
    ConcentricCircles((0, 0), F, A, R, 'g')
    for i in range(P+1):
        ConcentricCircles((np.cos(i*2*np.pi/P+np.pi/2),
                           np.sin(i*2*np.pi/P+np.pi/2)), F, A, R, 'g')


# 等比


# 向外
def wave_circle_pro_o(A, F, P, color, R=1):
    ConcentricCircles_Pro_o((0, 0), F, np.sqrt(A), R, color)
    for i in range(P+1):
        ConcentricCircles_Pro_o(
            ((np.cos(i*2*np.pi/P+np.pi/2)), np.sin(i*2*np.pi/P+np.pi/2)), F, np.sqrt(A), R, color)


# 向内
def wave_circle_pro_i(A, F, P, color, R=1):
    ConcentricCircles_Pro_i((0, 0), F, np.sqrt(A), R, color)
    for i in range(P+1):
        ConcentricCircles_Pro_i(
            ((np.cos(i*2*np.pi/P+np.pi/2)), np.sin(i*2*np.pi/P+np.pi/2)), F, np.sqrt(A), R, color)
# 双向


def wave_circle_pro(A, F, P, color, R=1):
    ConcentricCircles_Pro((0, 0), F, np.sqrt(A), R, color)
    for i in range(P+1):
        ConcentricCircles_Pro(
            ((np.cos(i*2*np.pi/P+np.pi/2)), np.sin(i*2*np.pi/P+np.pi/2)), F, np.sqrt(A), R, color)


# plt.axis('off')
# plt.show()
