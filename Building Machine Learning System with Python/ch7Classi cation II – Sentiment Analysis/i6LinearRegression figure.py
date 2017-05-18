import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

boston = load_boston()
# boston = boston.data
# print(boston[0:5], '#'*10, boston[:, 5][0:5])