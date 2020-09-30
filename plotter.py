from vekstrate import *
from functions import *


def plot1(medVekstrate, plt):
    plt.plot(x1, y1(x1), 'red', label='f(x)')
    if medVekstrate: vekstrate1(plt)
    return plt


def plot2(medVekstrate, plt):
    plt.plot(x2, y2(x2), 'blue', label='f(x)')
    if medVekstrate: vekstrate2(plt)


def plot3(medVekstrate, plt):
    plt.plot(x3, y3(x3), 'green', label='f(x)')
    if medVekstrate: vekstrate3(plt)


def plot4(medVekstrate, plt):
    plt.plot(x4, y4(x4), 'orange', label='f(x)')
    if medVekstrate: vekstrate4(plt)


def plotderivative1(plt):
    plt.plot(x1, dy1(x1), 'red', label='f(x)')


def plotderivative2(plt):
    plt.plot(x2, dy2(x2), 'blue', label='f(x)')


def plotderivative3(plt):
    plt.plot(x3, dy3(x3), 'green', label='f(x)')


def plotderivative4(plt):
    plt.plot(x4, dy4(x4), 'orange', label='f(x)')
