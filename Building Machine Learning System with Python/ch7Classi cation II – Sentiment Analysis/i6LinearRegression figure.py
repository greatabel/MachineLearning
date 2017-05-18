import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

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

ax.plot([0, boston.data[:, 5].max() + 1],
         [0, lr.predict(boston.data[:, 5].max() + 1)], '-', lw=4)
plt.show()