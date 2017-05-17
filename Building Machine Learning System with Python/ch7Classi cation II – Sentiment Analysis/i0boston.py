import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

boston = load_boston()
x = boston.data
y = boston.target

print(len(x), len(y),x[0:5], y[0:5])

# Fitting a model is trivial: call the ``fit`` method in LinearRegression:
lr = LinearRegression()
lr.fit(x, y)

# The instance member `residues_` contains the sum of the squared residues
rmse = np.sqrt(lr.residues_/len(x))
print('RMSE: {}'.format(rmse))