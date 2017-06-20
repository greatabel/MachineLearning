import math
import matplotlib.pyplot as plt
import numpy as np

def relu(x):
    y = x.copy()
    index = 0
    for val in x:
        y[index] = max(0, val)
        index += 1    
    return y

# https://en.wikipedia.org/wiki/Rectifier_(neural_networks)
x = np.arange(-100., 100., 0.2)
relu = relu(x)
plt.plot(x,relu)
plt.show()
