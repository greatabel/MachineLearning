import pylab as pl
import numpy as np

x = np.arange(-5,5,0.01)
s = 1
mu = 0
y = 1/(np.sqrt(2*np.pi)*s) * np.exp(-0.5*(x-mu)**2/s**2)
pl.plot(x,y,'k')

pl.show()