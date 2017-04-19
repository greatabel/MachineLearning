from termcolor import colored,cprint

import numpy as np
from scipy.optimize import curve_fit

def func(x,a,b,c):
    return a*np.exp( -(x-b)**2/(2*c**2) )

print(colored('generating clean data','green'))

x = np.linspace(0, 10, 20)
y = func(x, 1, 5, 2)

print('x=',x,'\ny=',y)

print(colored('adding noise to the data','blue'))
yn = y + 0.2 * np.random.normal(size=len(x))
print(colored(yn,'green'))

print(colored('executing curve_fit on noisy data','yellow'))
popt, pcov = curve_fit(func, x, yn)
print('popt=',popt,'pcov =', pcov)