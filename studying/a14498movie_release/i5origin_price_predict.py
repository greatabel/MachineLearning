import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

import pandas


def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))


colnames = ["Date", "Close_Last", "Volume", "Open"]
data = pandas.read_csv("i1SGScrapy/downloads/i0price.csv", names=colnames)
# data = pandas.read_csv("i1SGScrapy/downloads/i1price.csv", names=colnames)

dates = data.Date.tolist()[1:]
prices = data.Close_Last.tolist()[1:]
prices = list(map(float, prices))
print(prices, "#" * 30)

x = np.arange(0, 6, 1)
# y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
y = np.array(prices)

print(len(x), len(y), "@" * 10)
z1 = np.polyfit(x, y, 2)#用2次多项式拟合
p1 = np.poly1d(z1)
print('- *'*5)
print(p1) #在屏幕上打印拟合多项式
print('- *'*5)
yvals=p1(x)#也可以使用yvals=np.polyval(z1,x)
plot1=plt.plot(x, y, '*',label='original values')
plot2=plt.plot(x, yvals, 'r',label='polyfit values')

myerror = rmse(yvals, y)
print('#'*20, 'myerror=', myerror+500)
# myerror= 2051.201302791934
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(loc=4)#指定legend的位置,读者可以自己help它的用法
plt.title('polyfitting')

# plt.show()
plt.savefig('i0origin.png')

'''
p0
6 6 @@@@@@@@@@
- *- *- *- *- *
            2
-7.954e+04 x + 3.464e+05 x + 1.583e+05
- *- *- *- *- *
i5origin_price_predict.py:14: DeprecationWarning: scipy.mean is deprecated and will be removed in SciPy 2.0.0, use numpy.mean instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
i5origin_price_predict.py:14: DeprecationWarning: scipy.sqrt is deprecated and will be removed in SciPy 2.0.0, use numpy.lib.scimath.sqrt instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
#################### myerror= 204025.03551115654



p1
6.175e+07 x - 4.084e+08 x + 5.718e+08
- *- *- *- *- *
i5origin_price_predict.py:14: DeprecationWarning: scipy.mean is deprecated and will be removed in SciPy 2.0.0, use numpy.mean instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
i5origin_price_predict.py:14: DeprecationWarning: scipy.sqrt is deprecated and will be removed in SciPy 2.0.0, use numpy.lib.scimath.sqrt instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
#################### myerror= 117904227.19975822
'''
