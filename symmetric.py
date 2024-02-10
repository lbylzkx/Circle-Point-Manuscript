import numpy as np
import sys
sys.path.append('C:/Userslbylzk/Documents/BaiduSyncdisk/Flowers')


# 导入numpy模块


def symmetric_point(P1, P2, P):
    # 计算直线的斜率和截距
    # 如果两点的纵坐标相等，说明直线平行于x轴
    if P2[1] == P1[1]:
        # 两点连线平行于x轴，对称点的横坐标不变，纵坐标为2 * P1[1] - P[1]
        x_prime = P[0]
        y_prime = 2 * P1[1] - P[1]
    # 如果两点重合，说明直线不存在
    elif P2 == P1:
        # 两点重合，对称点不存在，返回None
        x_prime = None
        y_prime = None
    # 如果两点的横坐标不相等，说明斜率存在
    elif P2[0] != P1[0]:
        # 使用np.divide代替除法运算符，可以处理数组的运算
        k = np.divide(P2[1] - P1[1], P2[0] - P1[0])
        b = P1[1] - k * P1[0]
        # 计算直线的一般式的系数
        a = k
        c = -b
        # 计算对称点的坐标
        # 使用np.divide和np.power代替除法运算符和幂运算符，可以处理数组的运算
        # 用一个变量d来存储a * P[0] + b * P[1] + c的值，避免重复计算
        d = a * P[0] + b * P[1] + c
        x_prime = P[0] - 2 * np.divide(d, np.power(a, 2) + np.power(b, 2)) * a
        y_prime = P[1] - 2 * np.divide(d, np.power(a, 2) + np.power(b, 2)) * b
    # 如果两点的横坐标相等，说明斜率不存在
    else:
        k = None  # 将斜率设为None，表示无效值
        b = None  # 将截距设为None，表示无效值
        # 计算对称点的坐标
        # 两点连线垂直于x轴，对称点的横坐标为2 * P1[0] - P[0]，纵坐标不变
        x_prime = 2 * P1[0] - P[0]
        y_prime = P[1]
    # 返回对称点的坐标
    return [x_prime, y_prime]


# 定义一个函数，输入两个点的坐标和原点的坐标，输出对称点的坐标
def symmetric_point_s(x1, y1, x2, y2, x, y):
    # 计算直线的斜率和截距
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    # 计算直线的一般式的系数
    a = k
    c = -b
    # 计算对称点的坐标
    x_prime = x - 2 * (a * x + b * y + c) / (a ** 2 + b ** 2) * a
    y_prime = y - 2 * (a * x + b * y + c) / (a ** 2 + b ** 2) * b
    # 返回对称点的坐标
    return x_prime, y_prime


# 测试函数
x1, y1 = -1, -1  # 第一个点的坐标
x2, y2 = 0, 0  # 第二个点的坐标
x, y = 2, 1  # 原点的坐标
x_prime, y_prime = symmetric_point_s(x1, y1, x2, y2, x, y)  # 对称点的坐标
print(f"原点({x}, {y})关于直线({x1}, {y1})-({x2}, {y2})的对称点是({x_prime}, {y_prime})")

print(symmetric_point((-1, -1), (0, 0), (2, 1)))
