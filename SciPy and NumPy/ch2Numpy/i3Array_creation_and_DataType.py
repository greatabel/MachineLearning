import numpy as np

# First we create a list and then
# wrap it with the np.array() function. 
alist = [1, 2, 3]
arr = np.array(alist)
print('arr=', arr)

# Creating an array of zeros with five elements 
arr = np.zeros(5)
print('arr=', arr)

# What if we want to create an array going from 0 to 100? 
arr = np.arange(100)
print('arr=', arr)
