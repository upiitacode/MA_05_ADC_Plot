#!/usr/bin/python
import serial
import time

def getString(default_tty = 'ttyACM0'):
    nucleo = serial.Serial('/dev/' + default_tty,9600,timeout = 2)
    time.sleep(0.1)
    nucleo.flushInput()
    nucleo.readline()
    s = nucleo.readline()
    return  s.strip()

def main():
    print getString()

if __name__ == '__main__':
    main()
