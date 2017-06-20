from matplotlib.mlab import normpdf
# import matplotlib.numerix as nx
import numpy as np
import pylab as p

'''
http://scipy-cookbook.readthedocs.io/items/Matplotlib_SigmoidalFunctions.html

'''
# x = np.arange(-10, 10, 0.1)
# y = normpdf(x, 0, 1) # unit normal
# p.plot(x,y, color='red', lw=2)
# p.show()


def boltzman(x, xmid, tau):
    """
    evaluate the boltzman function with midpoint xmid and time constant tau
    over x
    """
    return 1. / (1. + np.exp(-(x-xmid)/tau))

x = np.arange(-6, 6, .01)
S = boltzman(x, 0, 1)
Z = 1-boltzman(x, 0.5, 1)
p.plot(x, S, x, Z, color='red', lw=2)
p.show()