import numpy as np

x = np.array([1, 2, 3 , 4])

assert np.mean(x) == np.sum(x) / len(x)

assert np.std(x) == np.sqrt(np.mean((x -np.mean(x)) ** 2 ))