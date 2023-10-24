# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:05:34 2023
APPLIED DATA SCIENCE 1
@author: Peter Adedeji
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)

#plot functions
plt.plot(x, np.sinh(x), label = 'sinh(x)')
plt.plot(x, np.cosh(x), label = 'cosh(x)')

#add labels
plt.xlabel('x')
plt.ylabel('f(x)')

plt.xlim(-6, 6)

#add legend
plt.legend(loc = 'bottom right')

#show plot
plt.show()
