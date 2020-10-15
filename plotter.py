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
    plt.plot(x1, f1(x1), 'red', label='f(x)')
    plt.plot(x1, df1(x1), 'yellow', label='df(x)')
    vekstrate = regnVekstrate(x1, f1)
    plt.plot(x1, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x1, f1, df1)
    plt.plot(x1, feil, 'blue', label='E(x)')
    plt.savefig('figurer/oppgave2a.png')
    labelPlot()


def plot2():
    plotSetup()
    plt.plot(x2, f2(x2), 'blue', label='f(x)')
    plt.plot(x2, df2(x2), 'yellow', label='df(x)')
    vekstrate = regnVekstrate(x2, f2)
    plt.plot(x2, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x2, f2, df2)
    plt.plot(x2, feil, 'blue', label='E(x)')
    plt.savefig('figurer/oppgave2b.png')
    labelPlot()


def plot3():
    plotSetup()
    plt.plot(x3, f3(x3), 'red', label='f(x)')
    plt.plot(x3, df3(x3), 'yellow', label='df(x)')
    vekstrate = regnVekstrate(x3, f3)
    plt.plot(x3, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x3, f3, df3)
    plt.plot(x3, feil, 'blue', label='E(x)')
    plt.savefig('figurer/oppgave2c.png')
    labelPlot()


def plot4():
    plotSetup()
    plt.plot(x4, f4(x4), 'red', label='f(x)')
    plt.plot(x4, df4(x4), 'yellow', label='df(x)')
    vekstrate = regnVekstrate(x4, f4)
    plt.plot(x4, vekstrate, 'purple', label='g(x)')
    feil = regnFeilpunkter(x4, f4, df4)
    plt.plot(x4, feil, 'blue', label='E(x)')
    plt.savefig('figurer/oppgave2d.png')
    labelPlot()


def regnVekstrate(intervall, funk):
    vekstrate = []
    for i in intervall:
        vekstrate.append(gx(i, funk))
    return vekstrate


def regnFeilpunkter(intervall, fx, dfx):
    feil = []
    for i in intervall:
        calcgx = gx(i, fx)
        feil.append(ex(dfx(i), calcgx))
        print(ex(dfx(i), calcgx))
    return feil
