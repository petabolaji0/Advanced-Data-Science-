# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 12:10:33 2023
ADS1
@author: pc
"""
#EXERCISE 3
# import standard math library
import numpy as np

# import standard graphics library
import matplotlib.pyplot as plt

# create an array with 10000 values
t = np.linspace(0, 2*(np.pi), 10000)

# define functions
def trigon1(a, b, j):
    x1 = (np.cos(a*t) - np.cos(b*t)**j)
    return x1

def trigon2(c, d, k):
    y1 = (np.sin(c*t) - np.sin(d*t)**k)
    return y1

# compute trigon1 and trigon2
x = trigon1(1, 60, 3)
y = trigon2(1, 120, 4)

# plot functions
plt.figure()
plt.plot(x,y)

# add label
plt.xlabel('x')
plt.ylabel('f(x)')

# change shape
plt.figure(figsize = (10, 10))
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# save plot
plt.savefig('ADS1.png')
plt.show()