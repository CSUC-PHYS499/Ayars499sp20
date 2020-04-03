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
import scipy.fftpack
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
'''
I'm not 100% sure what i'm doing here, but I looked up online how to do a 
fourier transform, and it works. However, I couldnt explain the reasoning behind
the terms xf and my yplot terms. The source code (or as i like to call it, 
"inspiration code") can be found at the url below

https://stackoverflow.com/questions/25735153/plotting-a-fast-fourier-transform-in-python
'''




N = len(time)
T = time[1] - time[0]

x = np.linspace(0.0, N*T, N)

a = np.array((time, x, time-x))

yf1 = scipy.fftpack.fft(x1)
yf2 = scipy.fftpack.fft(x2)
yf3 = scipy.fftpack.fft(x3)
yf4 = scipy.fftpack.fft(x4)
yf5 = scipy.fftpack.fft(x5)


#not sure why, but this makes it work. I'm pretty sure that it is due to a math
#method I am forgetting
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

yplot1 = 2.0/N * np.abs(yf1[:N//2])
yplot2 = 2.0/N * np.abs(yf2[:N//2])
yplot3 = 2.0/N * np.abs(yf3[:N//2])
yplot4 = 2.0/N * np.abs(yf4[:N//2])
yplot5 = 2.0/N * np.abs(yf5[:N//2])


plt.figure()
plt.plot(xf, yplot1, label="column 1")
plt.plot(xf, yplot2, label="column 2")
plt.plot(xf, yplot3, label="column 3")
plt.plot(xf, yplot4, label="column 4")
plt.plot(xf, yplot5, label="column 5")
plt.grid()
plt.legend()
plt.show()
