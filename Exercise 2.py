# import standard math library
import numpy as np

# import standard graphics library
import matplotlib.pyplot as plt

# create an array with 500 values
t = np.linspace(0, 2*(np.pi), 500)

#defining own function
def trigon1(a, b, j):
    x = (np.cos(a*t) - np.cos(b*t)**j)
    return x

y = trigon1(1, 60, 3)

#plot functions
plt.figure()
plt.plot(t, y)

#show plot
plt.show()
