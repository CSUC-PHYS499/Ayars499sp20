#!/usr/bin/env python

'''
	showdata.py
	Eric Ayars
	1/28/20

        Plots data in datafile.
'''

from pylab import *
from sys import argv

filename = argv[1]

t,x1,x2,x3,x4,x5 = loadtxt(filename, unpack=True, skiprows=2)

plot(t,x1, 'r-')
plot(t,x2, 'c-')
plot(t,x3, 'm-')
plot(t,x4, 'g-')
plot(t,x5, 'b-')

show()
