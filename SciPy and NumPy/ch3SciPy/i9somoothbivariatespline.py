from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np
from scipy.interpolate import SmoothBivariateSpline as SBS

# Defining a function
ripple = lambda x, y: np.sqrt(x**2 + y**2)+np.sin(x**2 + y**2)
# Generating sample that interpolation function will see 
xy= np.random.rand(1000, 2)
x, y = xy[:,0], xy[:,1]
print( colored( ('x, y = xy[:,0], xy[:,1]',x,'#',y),'blue') )

sample = ripple(xy[:,0] * 5 , xy[:,1] * 5)
# Interpolating data
fit = SBS(x * 5, y * 5, sample, s=0.01, kx=4, ky=4)
interp = fit(np.linspace(0, 5, 1000), np.linspace(0, 5, 1000))

print( colored( ('fit',fit,'interp',interp),'green') )
plt.plot(interp)
# plt.plot(grid_z0)
plt.show()