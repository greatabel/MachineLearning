from termcolor import colored,cprint

import numpy as np
import numpy.random as rand

arr = np.loadtxt("i10somefile.txt")
print('arr=',arr)

# http://stackoverflow.com/questions/16621351/how-to-use-python-numpy-savetxt-to-write-strings-and-float-number-to-an-ascii-fi
names  = np.array(['NAME_1', 'NAME_2', 'NAME_3'])
floats = np.array([ 0.1234 ,  0.5678 ,  0.9123 ])

ab = np.zeros(names.size, dtype=[('var1', 'S6'), ('var2', float)])
ab['var1'] = names
ab['var2'] = floats
print(colored( (names,'#',floats,'#',ab), 'red'))

np.savetxt('i11test.txt', ab, fmt="%10s %10.3f")