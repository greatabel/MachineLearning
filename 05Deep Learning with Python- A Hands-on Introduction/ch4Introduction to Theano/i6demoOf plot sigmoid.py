import math
import matplotlib.pyplot as plt
import numpy as np


# http://squall0032.tumblr.com/post/77300791096/plotting-a-sigmoid-function-using

def sigmoid(x):
    a = []
    for item in x:
        a.append(1/(1+math.exp(-item)))
    return a



x = np.arange(-10., 10., 0.2)
sig = sigmoid(x)
plt.plot(x,sig)
plt.show()
