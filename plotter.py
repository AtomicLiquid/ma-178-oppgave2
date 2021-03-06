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


def labelPlot(fignavn):
    plt.legend(loc='upper center')
    plt.savefig(fignavn)
    plt.show()


def plot1():
    plotSetup()
    plt.plot(x1, f1(x1), 'red', label='f(x)')
    plt.plot(x1, df1(x1), 'green', label='df(x)')
    vekstrate = regnVekstrate(x1, f1, dx1)
    plt.plot(x1, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x1, f1, df1, dx1)
    plt.plot(x1, feil, 'blue', label='E(x)')
    labelPlot('figurer/oppgave2a.png')


def plot2():
    plotSetup()
    plt.plot(x2, f2(x2), 'red', label='f(x)')
    plt.plot(x2, df2(x2), 'green', label='df(x)')
    vekstrate = regnVekstrate(x2, f2, dx2)
    plt.plot(x2, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x2, f2, df2, dx2)
    plt.plot(x2, feil, 'blue', label='E(x)')
    labelPlot('figurer/oppgave2b.png')


def plot3():
    plotSetup()
    plt.plot(x3, f3(x3), 'red', label='f(x)')
    plt.plot(x3, df3(x3), 'green', label='df(x)')
    vekstrate = regnVekstrate(x3, f3, dx3)
    plt.plot(x3, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x3, f3, df3, dx3)
    plt.plot(x3, feil, 'blue', label='E(x)')
    labelPlot('figurer/oppgave2c.png')


def plot4():
    plotSetup()
    plt.plot(x4, f4(x4), 'red', label='f(x)')
    plt.plot(x4, df4(x4), 'green', label='df(x)')
    vekstrate = regnVekstrate(x4, f4, dx4)
    plt.plot(x4, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x4, f4, df4, dx4)
    plt.plot(x4, feil, 'blue', label='E(x)')
    labelPlot('figurer/oppgave2d.png')


def regnVekstrate(intervall, funk, dx):
    vekstrate = []
    for i in intervall:
        vekstrate.append(gx(i, funk, dx))
    return vekstrate


def regnFeilpunkter(intervall, fx, dfx, dx):
    feil = []
    for i in intervall:
        calcgx = gx(i, fx, dx)
        feil.append(ex(dfx(i), calcgx))
    return feil
