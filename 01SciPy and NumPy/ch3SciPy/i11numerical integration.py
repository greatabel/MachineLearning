from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np
from scipy.integrate import quad, trapz

# Setting up fake data
x = np.sort(np.random.randn(8) * 4 + 4).clip(0,5) 
print( colored( ('x = np.sort(np.random.randn(150) * 4 + 4).clip(0,5) x = ','\n',x),'green') )
func = lambda x: np.sin(x) * np.cos(x ** 2) + 1
y = func(x)
print( colored( ('func = lambda x: np.sin(x) * np.cos(x ** 2) + 1 y = func(x) y=',y),'blue') )
# Integrating function with upper and lower 
# limits of 0 and 5, respectively
fsolution = quad(func, 0, 5)
dsolution = trapz(y, x=x)

print('fsolution = ' + str(fsolution[0]))
print('dsolution = ' + str(dsolution))
print('The difference is ' + str(np.abs(fsolution[0] - dsolution)))
