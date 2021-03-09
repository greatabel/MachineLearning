import math
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-100., 100., 0.2)
sig = np.tanh(x)
plt.plot(x,sig)
plt.show()
