import os

import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

CHART_DIR = "charts"

boston = load_boston()
# boston = boston.data
# print(boston[0:5], '#'*10, boston[:, 5][0:5])


# Index number five in the number of rooms
fig,ax = plt.subplots()
ax.scatter(boston.data[:, 5], boston.target)
ax.set_xlabel("Average number of rooms (RM)")
ax.set_ylabel("House Price")

x = boston.data[:, 5]
# print(x)
x = np.transpose(np.atleast_2d(x))
# print(x)

y = boston.target

lr = LinearRegression(fit_intercept=False)
lr.fit(x, y)

# set color of plot
# http://stackoverflow.com/questions/16006572/plotting-different-colors-in-matplotlib
ax.plot([0, boston.data[:, 5].max() + 1],
         [0, lr.predict(boston.data[:, 5].max() + 1)], '-', lw=4, color='r')
# plt.show()
fig.savefig(os.path.join(CHART_DIR, "Figure1.png"))

mse = mean_squared_error(y, lr.predict(x))
rmse = np.sqrt(mse)
print('RMSE (no intercept): {}'.format(rmse))


# Repeat, but fitting an intercept this time:
lr = LinearRegression(fit_intercept=True)

lr.fit(x, y)

fig,ax = plt.subplots()
ax.set_xlabel("Average number of rooms (RM)")
ax.set_ylabel("House Price")
ax.scatter(boston.data[:, 5], boston.target)
xmin = x.min()
xmax = x.max()
ax.plot([xmin, xmax], lr.predict([[xmin], [xmax]]) , '-', lw=4, color='r')
fig.savefig(os.path.join(CHART_DIR, "Figure2.png"))

mse = mean_squared_error(y, lr.predict(x))
print("Mean squared error (of training data): {:.3}".format(mse))

rmse = np.sqrt(mse)
print("Root mean squared error (of training data): {:.3}".format(rmse))

cod = r2_score(y, lr.predict(x))
print('COD (on training data): {:.2}'.format(cod))