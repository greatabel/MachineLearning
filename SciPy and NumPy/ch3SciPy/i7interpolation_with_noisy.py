from termcolor import colored,cprint

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
# Setting up fake data with artificial noise
sample = 30
x = np.linspace(1, 10 * np.pi, sample)
print( colored( ('x = np.linspace(1, 10 * np.pi, sample) x=',x),'green') )

y = np.cos(x) + np.log10(x) + np.random.randn(sample) / 10

print( colored( ('y = np.cos(x) + np.log10(x) + np.random.randn(sample) / 10 y=',y),'red') )
plt.plot(x, y)


# Interpolating the data
f = UnivariateSpline(x, y, s=1)

# x.min and x.max are used to make sure we do not 
# go beyond the boundaries of the data for the
# interpolation.
xint = np.linspace(x.min(), x.max(), 1000)
yint = f(xint)

print( colored( ('xint = np.linspace(x.min(), x.max(), 1000) xint=',xint),'blue') )
print( colored( ('yint = f(xint) yint=',yint),'green') )

plt.plot(xint, yint)
plt.show()