from termcolor import colored,cprint

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
# Defining a function
ripple = lambda x, y: np.sqrt(x**2 + y**2)+np.sin(x**2 + y**2)

# Generating gridded data. The complex number defines
# how many steps the grid data should have. Without the
# complex number mgrid would only create a grid data structure 
# with 5 steps.
grid_x, grid_y = np.mgrid[0:5:1000j, 0:5:1000j]
print( colored( ('grid_x=',grid_x, 'grid_y=',grid_y),'blue') )
# Generating sample that interpolation function will see 
xy = np.random.rand(1000, 2)
print( colored( xy,'green') )
sample = ripple(xy[:,0] * 5 , xy[:,1] * 5)
# Interpolating data with a cubic
grid_z0 = griddata(xy * 5, sample, (grid_x, grid_y), method='cubic')


plt.plot(xy, grid_z0)
# plt.plot(grid_z0)
plt.show()