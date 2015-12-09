#!/usr/bin/python

import plotter
import parser
import serial_nucleo

class Korosho:
    def getVal(this):
        dataString = serial_nucleo.getString()
        parsedDic = parser.parseString(dataString)
        return parsedDic['adc_ch1']


def main():
    korosho = Korosho()
    print korosho.getVal()
    plot = plotter.Plotter(korosho)
    plot.start()


if __name__ == '__main__':
    main()
