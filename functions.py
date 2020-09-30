import numpy as np

x1 = np.linspace(0, 2, 1000)
x2 = np.linspace(0, 2 * np.pi, 1000)
x3 = np.linspace(-2, 2, 1000)
x4 = np.linspace(0, 10, 1000)

dx = -0.00014


def y1(x):
    return 7 * x ** 2 - 8 * x + 1


def y2(x):
    return np.sin(x)


def y3(x):
    return (1 - x) / ((x + 3) ** 2)


def y4(x):
    return np.sqrt(1 + (x ** 2))


def dy1(x):
    return 14 * x - 8


def dy2(x):
    return np.cos(x)


def dy3(x):
    return (x - 5) / (x + 3) ** 3


def dy4(x):
    return x / np.sqrt(1 + x ** 2)


def gx(x, y):
    points = []
    for i in x:
        points.append((y(i + dx) - y(i)) / dx)
        print((y(i + dx) - y(i)) / dx)
    return points
