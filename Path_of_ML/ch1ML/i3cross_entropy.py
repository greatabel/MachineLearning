import numpy as np
from termcolor import colored

# https://stackoverflow.com/questions/47377222/cross-entropy-function-python

def cross_entropy(predictions, targets, epsilon=1e-12):
    """
    Computes cross entropy between targets (encoded as one-hot vectors)
    and predictions. 
    Input: predictions (N, k) ndarray
           targets (N, k) ndarray        
    Returns: scalar
    """
    predictions = np.clip(predictions, epsilon, 1. - epsilon)
    N = predictions.shape[0]
    ce = -np.sum(np.sum(targets*np.log(predictions+1e-9)))/N
    return ce


def main():
    predictions = np.array([[0.25,0.25,0.25,0.25],
                            [0.01,0.01,0.01,0.96]])
    targets = np.array([[0,0,0,1],
                       [0,0,0,1]])
    ans = 0.71355817782  #Correct answer
    x = cross_entropy(predictions, targets)
    print(np.isclose(x,ans))

if __name__ == "__main__":
    main()