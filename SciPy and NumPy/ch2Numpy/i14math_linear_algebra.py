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