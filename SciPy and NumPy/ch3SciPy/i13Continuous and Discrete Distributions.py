from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np
from scipy.stats import norm
# Set up the sample range 
x = np.linspace(-5,5,10)
# Here set up the parameters for the normal distribution,
# where loc is the mean and scale is the standard deviation. 
dist = norm(loc=0, scale=1)

# Retrieving norm's PDF and CDF 
pdf = dist.pdf(x)
cdf = dist.cdf(x)
# Here we draw out 500 random values from the norm. 
sample = dist.rvs(500)
print( colored( x,'green'),colored(dist,'red'), colored(pdf,'blue'),colored(cdf,'red'))
