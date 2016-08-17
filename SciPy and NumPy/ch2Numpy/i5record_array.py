import numpy as np

# Creating an array of zeros and defining column types 
recarr = np.zeros((2,), dtype=('i4,f4,a10'))
toadd = [(1,2.,'Hello'),(2,3.,"World")]
recarr[:] = toadd
print('recarr=', recarr)
