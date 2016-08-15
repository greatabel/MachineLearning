import numpy as np

# First we create a list and then
# wrap it with the np.array() function. 
alist = [1, 2, 3]
arr = np.array(alist)
print('alist = [1, 2, 3] np.array(alist)=', arr)

# Creating an array of zeros with five elements 
arr = np.zeros(5)
print('np.zeros(5)=', arr)

# What if we want to create an array going from 0 to 100? 
arr = np.arange(100)
print('np.arange(100)=', arr)

arr = np.arange(10,30)
print('np.array(10,30) =', arr)

arr = np.linspace(0,50,100)
print('np.linspace(0,1,100) =', arr)

# Or if you want to generate an array from 1 to 10 # in log10 space in 100 steps...
arr = np.logspace(0, 1, 100, base=10.0)
print('np.logspace(0, 1, 100, base=10.0) =', arr)

# Creating a 5x5 array of zeros (an image) 
image = np.zeros((5,5))
print('np.zeros((5,5)) =', image)

# Creating a 5x5x5 cube of 1's
# The astype() method sets the array with integer elements. 
cube = np.zeros((5,5,5)).astype(int) + 1
print('np.zeros((5,5,5)).astype(int) + 1 =', cube)

# Or even simpler with 16-bit floating-point precision... 
cube = np.ones((5, 5, 5)).astype(np.float16)
print('np.ones((5, 5, 5)).astype(np.float16) =', cube)

