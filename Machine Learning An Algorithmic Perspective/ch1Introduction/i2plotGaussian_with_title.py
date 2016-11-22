import pylab as pl
import numpy as np


gaussian = lambda x: 1/(np.sqrt(2*np.pi)*1.5)*np.exp(-(x-0)**2/(2*(1.5**2)))
x = np.arange(-5, 5, 0.5)
y = gaussian(x)

# print('x=', x, '\ny=', y)
pl.plot(x, y, 'k', linewidth=3, marker='o')
pl.xlabel('XXX')
pl.ylabel('Y(X)')
pl.axis([-5,5,0,0.3])
pl.title('Gaussian Function ( mean 0, standard deviation 1.5)')

pl.show()
