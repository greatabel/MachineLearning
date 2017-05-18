
import numpy as np
# from sklearn.cross_validation import KFold
from sklearn.model_selection import KFold

from sklearn.linear_model import LinearRegression, ElasticNet, Lasso, Ridge
from sklearn.metrics import r2_score
from sklearn.datasets import load_boston

boston = load_boston()
x = boston.data
y = boston.target