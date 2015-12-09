#!/usr/bin/python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy
import math


def createEmpyList(size = 0, initVal = 0):
    newList = []
    for i in range(size):
        newList.append(initVal)
    return newList

class Plotter:
    def __init__(this,valgenerator):
        this.generator = valgenerator
        this.data = list(numpy.linspace(0,4096,50))

        x = range(50)
        this.fig, this.ax = plt.subplots()
        this.line, = this.ax.plot(x,this.data)

    def updateData(this):
        newVal = this.generator.getVal()
        this.data.pop(0)
        this.data.append(newVal)

    def animate(this,i):
        this.updateData()
        this.line.set_ydata(this.data)
        return this.line,

    def init(this):
        this.updateData()
        this.line.set_ydata(this.data)
        return this.line,

    def start(this):
        ani = animation.FuncAnimation(this.fig, this.animate, numpy.arange(0,200), init_func = this.init, interval = 100, blit = True)
        plt.show()


class Korosho:
    def __init__(this, i = 0):
        this.i = 0
    def getVal(this):
        this.i += 1
        return this.i

def main():
    korosho = Korosho(3)
    plotter = Plotter(korosho)
    plotter.start()


if __name__ == '__main__':
    main()

