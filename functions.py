import numpy as np

x1 = np.linspace(0, 2, 1000)
x2 = np.linspace(0, 2 * np.pi, 1000)
x3 = np.linspace(-2, 2, 1000)
x4 = np.linspace(0, 10, 1000)

dx = 0.001


def f1(x):
    return 7 * x ** 2 - 8 * x + 1


def f2(x):
    return np.sin(x)


def f3(x):
    return (1 - x) / ((x + 3) ** 2)


def f4(x):
    return np.sqrt(1 + (x ** 2))


# df = deriverte av f(x)
def df1(x):
    return 14 * x - 8


def df2(x):
    return np.cos(x)


def df3(x):
    return (x - 5) / (x + 3) ** 3


def df4(x):
    return x / np.sqrt(1 + x ** 2)


# Funksjon for beregning av vekstrate
def gx(x, y):
    return (y(x + dx) - y(x)) / dx


def ex(dfx, calcgx):
    return np.abs(dfx - calcgx)
