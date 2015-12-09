#!/usr/bin/python

import re

def parseString(lectura):
    lectura_separada = re.findall('(\w+)\s*=\s*(-?\d+)',lectura)
    lectura_pro = {}
    for par in lectura_separada:
        lectura_pro[par[0]] = int(par[1])
    return lectura_pro

def main():
    print parseString('adc_channel_1 = 2340')

if __name__ == '__main__':
    main()
