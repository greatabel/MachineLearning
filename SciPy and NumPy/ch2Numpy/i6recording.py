from termcolor import colored
import numpy as np

# Creating an array of zeros and defining column types 
recarr = np.zeros((2,), dtype=('i4,f4,a10'))
print('recarr=', recarr)
# Now creating the columns we want to put # in the recarray
col1 = np.arange(2) + 10
col2 = np.arange(2, dtype=np.float32) 
col3 = ['Hello', 'World']
print(colored("col1 = np.arange(2) + 10   col2 = np.arange(2, dtype=np.float32)  col3 = ['Hello', 'World'] ", 'blue'))
print('col1,col2,col3=',col1,col2,col3)
# Here we create a list of tuples that is # identical to the previous toadd list. 
# toadd = zip(col1, col2, col3)
# python3 not zip
toadd = list(zip(col1, col2, col3))


print('toadd=', toadd)
# Assigning values to reca
recarr[:] = toadd
print('recarr=', recarr)
# Assigning names to each column, which
# are now by default called 'f0', 'f1', and 'f2'.
recarr.dtype.names = ('Integers' , 'Floats', 'Strings')
# If we want to access one of the columns by its name, we # can do the following.
# http://stackoverflow.com/questions/18186936/errornumpy-narray-object-not-callable
print("\nrecarr['Integers']=",recarr['Integers'])
# array([1, 2], dtype=int32)