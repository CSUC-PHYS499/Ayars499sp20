# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:33:45 2020

@author: Sean Dillon

This file is designed to compute a Fourier Transform of data that will be 
aquired scientifically. It is expected that the file name will be changed when
a new data file is given. Or you could rename your data file to be called 
fakedata.txt. It really is up to you honestly. 

This file assumes that your text file has dimensions of Nx6, with the first 
column being time.
"""

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
plt.close('all')
#starting out by importing the 3 libraries we always use

data = np.loadtxt("fakedata.txt")
#importing our data from a .txt file. After importing this, it shows us that 
#our column headers are automatically removed, thus making it exceptionally 
#easier to use



time = data[:,0]
#assuming time is the first column

x1 = data[:,1]
x2 = data[:,2]
x3 = data[:,3]
x4 = data[:,4]
x5 = data[:,5]
#all other columns. I kept the same headers used in the .txt file for simplicity
#despite my objections to starting data at 1. 

plt.figure()
plt.plot(time, x1)
plt.plot(time, x2)
plt.plot(time, x3)
plt.plot(time, x4)
plt.plot(time, x5)
plt.show()

x1_fft = np.fft.fft(x1)
plt.figure()
plt.plot(x1, x1_fft)
plt.show()



