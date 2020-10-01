from vekstrate import *
from functions import *
import matplotlib.pyplot as plt


def plotSetup():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('zero')  # Y-aksen
    ax.spines['bottom'].set_position('zero')  # X-aksen
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')


def plotSetup2():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')  # Y-aksen
    ax.spines['bottom'].set_position('center')  # X-aksen
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')


def labelPlot():
    plt.legend(loc='lower right')
    plt.show()


def plot1():
    plotSetup()
    plt.plot(x1, y1(x1), 'red', label='f(x)')
    labelPlot()
    print("hello byezZz")


def plot2():
    plotSetup()
    plt.plot(x2, y2(x2), 'blue', label='f(x)')
    labelPlot()


def plot3():
    plotSetup()
    plt.plot(x3, y3(x3), 'green', label='f(x)')
    labelPlot()


def plot4():
    plotSetup()
    plt.plot(x4, y4(x4), 'orange', label='f(x)')
    labelPlot()


def plotderivative1():
    plotSetup()
    plt.plot(x1, dy1(x1), 'red', label='f(x)')
    labelPlot()


def plotderivative2():
    plotSetup()
    plt.plot(x2, dy2(x2), 'blue', label='f(x)')
    labelPlot()


def plotderivative3():
    plotSetup2()
    plt.plot(x3, dy3(x3), 'green', label='f(x)')
    labelPlot()


def plotderivative4():
    plotSetup()
    plt.plot(x4, dy4(x4), 'orange', label='f(x)')
    labelPlot()


def vekst1():
    plotSetup()
    plt.plot(x1, y1(x1), 'red', label='f(x)')
    plt.plot(x1, gx(x1, y1), 'purple', label='vekstrate')
    labelPlot()


def vekst2():
    plotSetup()
    plt.plot(x2, y2(x2), 'blue', label='f(x)')
    plt.plot(x2, gx(x2, y2), 'purple', label='vekstrate')
    labelPlot()


def vekst3():
    plotSetup()
    plt.plot(x3, y3(x3), 'green', label='f(x)')
    plt.plot(x3, gx(x3, y3), 'purple', label='vekstrate')
    labelPlot()



def vekst4():
    plotSetup()
    plt.plot(x4, y4(x4), 'orange', label='f(x)')
    plt.plot(x4, gx(x4, y4), 'purple', label='vekstrate')
    labelPlot()