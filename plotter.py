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
    plt.plot(x1, f1(x1), 'red', label='f(x) = 7 * x ** 2 - 8 * x + 1')
    labelPlot()
    plt.savefig('figurer/oppgave2a1.png')


def plot2():
    plotSetup()
    plt.plot(x2, f2(x2), 'blue', label='f(x) = sin(x)')
    labelPlot()
    plt.savefig('figurer/oppgave2a2.png')


def plot3():
    plotSetup()
    plt.plot(x3, f3(x3), 'green', label='f(x) = (1 - x) / ((x + 3) ** 2)')
    labelPlot()
    plt.savefig('figurer/oppgave2a3.png')


def plot4():
    plotSetup()
    plt.plot(x4, f4(x4), 'orange', label='f(x) = sqrt(1 + (x ** 2))')
    labelPlot()
    plt.savefig('figurer/oppgave2a4.png')


def plotderivative1():
    plotSetup()
    plt.plot(x1, df1(x1), 'red', label='df(x) = 14 * x - 8')
    labelPlot()
    plt.savefig('figurer/oppgave2b1.png')


def plotderivative2():
    plotSetup()
    plt.plot(x2, df2(x2), 'blue', label='df(x) = cos(x)')
    labelPlot()
    plt.savefig('figurer/oppgave2b2.png')


def plotderivative3():
    plotSetup2()
    plt.plot(x3, df3(x3), 'green', label='df(x) = (x - 5) / (x + 3) ** 3')
    labelPlot()
    plt.savefig('figurer/oppgave2b3.png')


def plotderivative4():
    plotSetup()
    plt.plot(x4, df4(x4), 'orange', label='df(x) = x / sqrt(1 + x ** 2)')
    labelPlot()
    plt.savefig('figurer/oppgave2b4.png')


def vekst1():
    plotSetup()
    plt.plot(x1, f1(x1), 'red', label='f(x) = 7 * x ** 2 - 8 * x + 1')
    vekstrate = regnVekstrate(x1, f1)
    plt.plot(x1, vekstrate, 'purple', label='vekstrate')
    labelPlot()
    plt.savefig('figurer/oppgave2c1.png')


def vekst2():
    plotSetup()
    plt.plot(x2, f2(x2), 'blue', label='f(x) = sin(x)')
    vekstrate = regnVekstrate(x2, f2)
    plt.plot(x2, vekstrate, 'purple', label='vekstrate')
    labelPlot()
    plt.savefig('figurer/oppgave2c2.png')


def vekst3():
    plotSetup()
    plt.plot(x3, f3(x3), 'green', label='f(x) = (1 - x) / ((x + 3) ** 2)')
    vekstrate = regnVekstrate(x3, f3)
    plt.plot(x3, vekstrate, 'purple', label='vekstrate')
    labelPlot()
    plt.savefig('figurer/oppgave2c3.png')


def vekst4():
    plotSetup()
    plt.plot(x4, f4(x4), 'orange', label='f(x) = sqrt(1 + (x ** 2))')
    vekstrate = regnVekstrate(x4, f4)
    plt.plot(x4, vekstrate, 'purple', label='vekstrate')
    labelPlot()
    plt.savefig('figurer/oppgave2c4.png')


def feil1():
    plotSetup()
    feil = regnFeilpunkter(x1, f1)
    plt.plot(x1, feil, 'red', label='E(x)')
    labelPlot()
    plt.savefig('figurer/oppgave2d1.png')


def feil2():
    plotSetup()
    feil = regnFeilpunkter(x2, f2)
    plt.plot(x2, feil, 'red', label='E(x)')
    labelPlot()
    plt.savefig('figurer/oppgave2d2.png')


def feil3():
    plotSetup()
    feil = regnFeilpunkter(x3, f3)
    plt.plot(x3, feil, 'red', label='E(x)')
    labelPlot()
    plt.savefig('figurer/oppgave2d3.png')


def feil4():
    plotSetup()
    feil = regnFeilpunkter(x4, f4)
    plt.plot(x4, feil, 'red', label='E(x)')
    labelPlot()
    plt.savefig('figurer/oppgave2d4.png')


def regnFeilpunkter(intervall, funk):
    feil = []
    for i in intervall:
        calcgx = gx(i, funk)
        feil.append(ex(funk(i), calcgx))
    return feil


def regnVekstrate(intervall, funk):
    vekstrate = []
    for i in intervall:
        vekstrate.append(gx(i, funk))
    return vekstrate
