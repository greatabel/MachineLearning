import os
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot as plt

import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

CHART_DIR = "charts"

boston = load_boston()

x = boston.data
y = boston.target

lr = LinearRegression()
lr.fit(x, y)
p = lr.predict(x)
print("RMSE: {:.2}.".format(np.sqrt(mean_squared_error(y, p))))
print("R2: {:.2}.".format(lr.score(x, y)))

fig,ax = plt.subplots()
ax.scatter(p, y)
ax.set_xlabel('Predicted price')
ax.set_ylabel('Actual price')
ax.plot([y.min(), y.max()], [y.min(), y.max()], lw=4,  color='g')

fig.savefig(os.path.join(CHART_DIR, "Figure4.png"))
