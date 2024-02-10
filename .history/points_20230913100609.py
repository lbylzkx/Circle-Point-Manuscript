from fractions import Fraction
import matplotlib.pyplot as plt


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
    return [two(n-1), two(n-1), two(n), 0, -two(n), -two(n), -two(n+1), 0]


# Tests
# print(two(1),two(2),two(3),two(4),two(5))
while True:
    n = int(input("Enter cycles:"))
    x = x_squence(n)
    y = y_squence(n)
    for i, a in enumerate(x):
        x[i] = Fraction(a).limit_denominator()
    for i, a in enumerate(y):
        y[i] = Fraction(a).limit_denominator()
    print(x)
    print(y)
    plot = plt.plot(x, y, 'ro')
    plot.show()
