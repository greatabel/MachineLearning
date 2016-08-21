from termcolor import colored,cprint

from scipy.optimize import fsolve 
import numpy as np

line = lambda x: x + 3
solution = fsolve(line, -2) 
print(solution)
