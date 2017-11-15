import numpy as np
from termcolor import colored

def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

