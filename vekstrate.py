from functions import *
import matplotlib.pyplot as plt
from plotter import *


def vekstrate1():
    plt.plot(x1, y1(x1), 'red', label='f(x)')
    plt.plot(x1, gx(x1, y1), 'purple', label='vekstrate')




def vekstrate2():
    plotSetup()
    plt.plot(x2, gx(x2, y2), 'purple', label='vekstrate')



def vekstrate3():
    plotSetup()
    plt.plot(x3, gx(x3, y3), 'purple', label='vekstrate')
    labelPlot()


def vekstrate4():
    plotSetup()
    plt.plot(x4, gx(x4, y4), 'purple', label='vekstrate')
    labelPlot()
