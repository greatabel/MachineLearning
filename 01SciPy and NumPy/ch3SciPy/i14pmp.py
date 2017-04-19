from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np
from scipy.stats import geom
# Here set up the parameters for the geometric distribution. 

p = 0.5
dist = geom(p)
# Set up the sample range. 
x = np.linspace(0, 5, 10)
# Retrieving geom's PMF and CDF 
pmf = dist.pmf(x)
cdf = dist.cdf(x)
# Here we draw out 500 rand
print( colored( x,'green'),colored(dist,'red'), colored(pmf,'blue'),colored(cdf,'red'))