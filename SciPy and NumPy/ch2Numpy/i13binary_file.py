from termcolor import colored,cprint

import numpy as np

data = np.empty((1000,1000))
# np.save('test.npy', data)

# If space is an issue for large files, then 
# use numpy.savez instead. It is slower than 
# numpy.save because it compresses the binary 
# file.
# np.save('test.npy', data)
# # Loading the data array 
# newdata = np.load('test.npy')

np.savez('test.npz', data)
# Loading the data array 
newdata = np.load('test.npz')

print(colored( newdata, 'blue'))