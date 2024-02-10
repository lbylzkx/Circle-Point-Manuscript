from fractions import Fraction
import matplotlib.pyplot as plt
import numpy as np


def get_x_n(i):
    if i == 1:
        return 1
    else:
        return get_x_n(i-1)+4


def get_y_n(i):
    if i == 1:
        return 1
    else:
        return get_y_n(i-1)+3


def two(n):
    return 1/2**n


def x_squence(i):
    n = get_x_n(i)
    return [-two(n-1), 0, two(n), two(n), two(n+1), 0, -two(n+2), -two(n+2)]


def y_squence(i):
    n = get_y_n(i)
    return [two(n-1), two(n-1), two(n), 0, -two(n+1), -two(n+1), -two(n+2), 0]


# Tests
# print(two(1),two(2),two(3),two(4),two(5))
while True:
    n = int(input("Enter cycles:"))
    x_all = []
    for i in range(n):
        x_i = x_squence(i+1)
        x_all = x_all + [x_i]
    x = [element for sublist in x_all for element in sublist]
    # print(x)

    y_all = []
    for i in range(n):
        y_i = y_squence(i+1)
        y_all = y_all + [y_i]
    y = [element for sublist in y_all for element in sublist]
    # print(y)

    """
    see in Fraction
    """
    # x = x_squence(n)
    # y = y_squence(n)
    for i, a in enumerate(x):
        x[i] = Fraction(a).limit_denominator()
    for i, a in enumerate(y):
        y[i] = Fraction(a).limit_denominator()
    print(x)
    print(y)
    plt = plt.plot(x, y)


# generrate points using 三角函数
