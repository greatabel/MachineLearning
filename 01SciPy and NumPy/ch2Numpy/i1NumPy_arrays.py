import numpy as np

# create an array with 10^7 elements

arr = np.arange(1e7)

#converting ndarrray to list
larr = arr.tolist()

def list_times(alist, scalar):
    for i, val in enumerate(alist):
        alist[i] = val*scalar
    return alist

# http://stackoverflow.com/questions/10361206/how-to-run-an-ipython-magic-from-a-script-or-timing-a-python-script
# 允许需要：ipython i1NumPy_arrays.py
from IPython import get_ipython
ipython = get_ipython()

ipython.magic("timeit arr * 1.1") 

ipython.magic("timeit list_times(larr, 1.1)") 


