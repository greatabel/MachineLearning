from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np


import numpy as np
from scipy import stats
# Generating a normal distribution sample # with 100 elements
sample = np.random.randn(20)
print( colored( ('sample',sample),'green') )
# normaltest tests the null hypothesis. 
out = stats.normaltest(sample) 
print('normaltest output') 
print('Z-score = ' + str(out[0])) 
print('P-value = ' + str(out[1]))
# kstest is the Kolmogorov-Smirnov test for goodness of fit.
# Here its sample is being tested against the normal distribution. 
# D is the KS statistic and the closer it is to 0 the better.
out = stats.kstest(sample, 'norm')
print('\nkstest output for the Normal distribution')
print('D = ' + str(out[0]))
print('P-value = ' + str(out[1]))
# Similarly, this can be easily tested against other distributions, 
# like the Wald distribution.
out = stats.kstest(sample, 'wald')
print('\nkstest output for the Wald distribution')
print('D = ' + str(out[0])) 
print('P-value = ' + str(out[1]))