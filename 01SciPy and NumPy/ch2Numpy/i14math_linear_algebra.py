from termcolor import colored,cprint

import numpy as np

# define matrices
A = np.matrix([
    [3,6,-5],
    [1,-3,2],
    [5,-1,4]
    ])

B = np.matrix(
    [
    [12],
    [-2],
    [10]
    ]
    )

# solving the variables
X = A ** (-1) * B

print(X)

print(colored('method 2# without directly invoking the numpy.matrix class.)','green'))
a = np.array([[3, 6, -5], 
    [1, -3, 2],
    [5, -1, 4]])
# Defining the array
b = np.array([12, -2, 10])
print('Solving for the variables, where we invert A :x = np.linalg.inv(a).dot(b)')
x = np.linalg.inv(a).dot(b)
print(x)

