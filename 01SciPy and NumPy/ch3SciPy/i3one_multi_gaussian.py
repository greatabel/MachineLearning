from termcolor import colored,cprint

import numpy as np
from scipy.optimize import curve_fit

# Two-Gaussian model
def func(x, a0, b0, c0, a1, b1,c1):
    return a0*np.exp(-(x - b0) ** 2/(2 * c0 ** 2))\
        + a1 * np.exp(-(x - b1) ** 2/(2 * c1 ** 2))


# Generating clean data
x = np.linspace(0, 20, 200)
y = func(x, 1, 3, 1, -2, 15, 0.5)
# Adding noise to the data
yn = y + 0.2 * np.random.normal(size=len(x))

# Since we are fitting a more complex function, 
# providing guesses for the fitting will lead to 
# better results.
guesses = [1, 3, 1, 1, 15, 1]

# Executing curve_fit on noisy data 
popt, pcov = curve_fit(func, x, yn,
        p0=guesses)
print(popt,colored('#\n','green'), pcov)