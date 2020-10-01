import numpy as np

x1 = np.linspace(0, 2, 1000)
x2 = np.linspace(0, 2 * np.pi, 1000)
x3 = np.linspace(-2, 2, 1000)
x4 = np.linspace(0, 10, 1000)

dx = -0.00014


def y1(x):
    y1 = 7 * x ** 2 - 8 * x + 1
    return y1



def y2(x):
    y2 = np.sin(x)
    return y2


def y3(x):
    y3 = (1 - x) / ((x + 3) ** 2)
    return y3


def y4(x):
    y4 = np.sqrt(1 + (x ** 2))
    return y4


def dy1(x):
    dy1 = 14 * x - 8
    return dy1


def dy2(x):
    dy2 = np.cos(x)
    return dy2


def dy3(x):
    dy3 = (x - 5) / (x + 3) ** 3
    return dy3


def dy4(x):
    dy4 = x / np.sqrt(1 + x ** 2)
    return dy4


def gx(x, y):
    points = []
    for i in x:
        points.append((y(i + dx) - y(i)) / dx)
        print((y(i + dx) - y(i)) / dx)
    return points
