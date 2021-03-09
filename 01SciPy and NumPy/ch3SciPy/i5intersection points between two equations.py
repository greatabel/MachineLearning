from termcolor import colored,cprint
from scipy.optimize import fsolve 
import numpy as np
# Defining function to simplify intersection solution 
def findIntersection(func1, func2, x0):
    return fsolve(lambda x : func1(x) - func2(x), x0)

# Defining functions that will intersect
funky = lambda x : np.cos(x / 5) * np.sin(x / 2) 
line = lambda x : 0.01 * x - 0.5
# Defining range and getting solutions on intersection points
x = np.linspace(0,45,100)
result = findIntersection(funky, line, [15, 20, 30, 35, 40, 45])
# Printing out results for x and y print(result, line(result))

# Printing out results for x and y 
print(colored('###\n','green'),result,colored('###\n','blue'), line(result))
