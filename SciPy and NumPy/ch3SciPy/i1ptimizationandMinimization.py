from termcolor import colored,cprint

import numpy as np
from scipy.optimize import curve_fit

# creating a function to model and create data
def func(x,a,b):
    return a * x + b

# generate clean data
# numpy.linspace(start, stop, num=50)
x = np.linspace(0,10, 100)
y = func(x, 1, 2)
print(colored(('x=',x,'\ny=',y),'green'))

# add noise to the data
yn = y + 0.9 * np.random.normal(size=len(x))
print(colored(('yn=',yn),'blue'))

# executing curve_fit on noisy data
popt, pcov = curve_fit(func, x, yn)

# popt returns the best fit values
print(popt)