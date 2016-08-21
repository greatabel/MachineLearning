import numpy as np
from scipy.interpolate import interp1d
# Setting up fake data
x = np.linspace(0, 10 * np.pi, 20) 
y = np.cos(x)
# Interpolating data
fl = interp1d(x, y, kind='linear')
fq = interp1d(x, y, kind='quadratic')
# x.min and x.max are used to make sure we do not # go beyond the boundaries of the data for the
# interpolation.
xint = np.linspace(x.min(), x.max(), 10)
yintl = fl(xint) 
yintq = fq(xint)
print(yintl,'#\n', yintq)