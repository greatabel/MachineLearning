import numpy as np

# Creating an array of zeros and defining column types 
recarr = np.zeros((2,), dtype=('i4,f4,a10'))

toadd = [(1,2.,'Hello'),(2,3.,"World")]
recarr[:] = toadd
print('recarr=', recarr )

recarrA = np.zeros((2,), dtype=('f2,f4,a5'))
print('recarrA=', recarrA)
recarrA[:] = [(1.111111,2.11111111111,'abcdefghijklmnopqrst'),(11.111111,22.11111111111,'1abcdefghijklmnopqrst')]
print('recarrA=', recarrA )

