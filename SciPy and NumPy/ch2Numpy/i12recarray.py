from termcolor import colored,cprint

import numpy as np
# i12example.txt content is :
# XR21 32.789 1
# XR22 33.091 2

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
table = np.loadtxt('i12example.txt',
        dtype={'names': ('ID', 'Result', 'Type'),
        'formats': ('S4', 'f4', 'i2')})
print('table=', table,"\ntable['Result']=",table['Result'])