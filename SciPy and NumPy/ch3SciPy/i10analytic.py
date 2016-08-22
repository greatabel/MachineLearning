from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np
from scipy.integrate import quad

# Defining function to integrate
func = lambda x: np.cos(np.exp(x)) ** 2
# Integrating function with upper and lower 
# limits of 0 and 3, respectively
solution = quad(func, 0, 3)
print(solution)

x = np.linspace(0, 3, 100)
y = np.cos(np.exp(x))

plt.plot(x,y)
plt.show()