import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from scipy.stats import norm
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

import pandas
import math
import time
import datetime
import pickle
# https://www.boxofficemojo.com/
# datasource

def sentiment_improve(base, vote):
    M = math.e*base*100
    upper = 50
    down = 30
    a = M + math.log(math.e **vote)
    b = M + math.log(math.e ** 1)

    r = a / b
    print('sentiment_improve a,b=',a, b, 'result=', r)
    return r
    # n = math.log(r)
    # print('n=', n)

# sentiment_improve()
# time.sleep(100)


colnames = ["Date", "Close_Last", "Volume", "Open"]
# data = pandas.read_csv("i1SGScrapy/downloads/i0price.csv", names=colnames)
data = pandas.read_csv("i1SGScrapy/downloads/i1price.csv", names=colnames)

dates = data.Date.tolist()[1:]
mydates = []
# print('dates=', dates)
for d in dates:
    # fd = datetime.datetime.strptime(d, '%m/%d/%Y').strftime( '%Y-%m-%d')
    mydates.append(int(d))
print(len(mydates),'mydates=', mydates)
prices = data.Close_Last.tolist()[1:]
prices = list(map(float, prices))





hot_dict = {}
sentiment_dict = {}
hots = []
sentiments = []
with open("hot.pickle", "rb") as handle:
    hot_dict = pickle.load(handle)
# print(hot_dict, '#@'*30)

if len(hot_dict)!=6:
    hot_dict = {0:10, 1: 10, 2: 20, 3:10, 4:10, 5:20}


with open("sentiment_dict.pickle", "rb") as handle:
    sentiment_dict = pickle.load(handle)

if len(sentiment_dict)!= 6:
    sentiment_dict = {0:0.9, 1: 0.99, 2: 0.8, 3:0.8, 4:0.8, 5:0.75}
for key, value in hot_dict.items():
    # print(key, '#',value)
    if key in mydates:
        print('choose:', key, '#',value)
        hots.append(value)

print('\n'*5)
for key, value in sentiment_dict.items():
    if key in mydates:
        print('choose:', key, '#',value)
        sentiments.append(value)

print(hots, '$'*20, sentiments)
print('len(hots)=', len(hots))


newprcies = []
for i in range(0, len(hots)):
    print(i)
    r = sentiment_improve(hots[i], sentiments[i])
    p = prices[i]* r
    newprcies.append(p)

print('price ', '->'*10)
print(prices, "#" * 30)
print(newprcies, '@'*20)
# time.sleep(100)

x = np.arange(0, 6, 1)
print(x)

# y = np.array([4.00, 6.40, 8.00, 8.80, 9.22, 9.50, 9.70, 9.86, 10.00, 10.20, 10.32, 10.42, 10.50, 10.55, 10.58, 10.60])
y = np.array(newprcies)

print(len(x), len(y), "@" * 10)




def rmse(y_test, y):
    return sp.sqrt(sp.mean((y_test - y) ** 2))


"""'' 与均值相比的优秀程度，介于[0~1]。0表示不如均值。1表示完美预测.这个版本的实现是参考scikit-learn官网文档  """


def R2(y_test, y_true):
    return 1 - ((y_test - y_true) ** 2).sum() / ((y_true - y_true.mean()) ** 2).sum()


def R22(y_test, y_true):
    y_mean = np.array(y_true)
    y_mean[:] = y_mean.mean()
    return 1 - rmse(y_test, y_true) / rmse(y_mean, y_true)


plt.scatter(x, y, s=5)
degree = [1, 2, 3, 100]
y_test = []
y_test = np.array(y_test)


for d in degree:
    print('\n'*3, d, '\n')
    clf = Pipeline(
        [
            ("poly", PolynomialFeatures(degree=d)),
            ("linear", LinearRegression(fit_intercept=False)),
        ]
    )
    clf.fit(x[:, np.newaxis], y)
    y_test = clf.predict(x[:, np.newaxis])
    print('y_test=>', y_test, '\n')
    print(" start ->" * 10, d)
    print("coef=> ",clf.named_steps["linear"].coef_)

    print(" end ->" * 10, d)
    print(
        "###rmse=%.2f, R2=%.2f, R22=%.2f, clf.score=%.2f"
        % (
            rmse(y_test, y),
            R2(y_test, y),
            R22(y_test, y),
            clf.score(x[:, np.newaxis], y),
        )
    )

    plt.plot(x, y_test, linewidth=2)
'''
p0
y_test=> [ 41948.05301955 588029.73598694 626022.69452464 388609.73701278
 108473.67183151  18297.30736095] 

 start -> start -> start -> start -> start -> start -> start -> start -> start -> start -> 3
coef=>  [  41948.05301955  877686.98130894 -370385.76640491   38780.46806336]
 end -> end -> end -> end -> end -> end -> end -> end -> end -> end -> 3
i6advanced_price_sentiment_cor.py:128: DeprecationWarning: scipy.mean is deprecated and will be removed in SciPy 2.0.0, use numpy.mean instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
i6advanced_price_sentiment_cor.py:128: DeprecationWarning: scipy.sqrt is deprecated and will be removed in SciPy 2.0.0, use numpy.lib.scimath.sqrt instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
###rmse=158673.20, R2=0.72, R22=0.47, clf.score=0.72


p1
 3 

y_test=> [ 6.66958146e+08  9.20282029e+07 -7.40083425e+07 -2.14207148e+07
  5.95218610e+07 -2.14498402e+07] 

 start -> start -> start -> start -> start -> start -> start -> start -> start -> start -> 3
coef=>  [ 6.66958146e+08 -8.42799718e+08  2.99581312e+08 -3.17115375e+07]
 end -> end -> end -> end -> end -> end -> end -> end -> end -> end -> 3
i6advanced_price_sentiment_cor.py:108: DeprecationWarning: scipy.mean is deprecated and will be removed in SciPy 2.0.0, use numpy.mean instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
i6advanced_price_sentiment_cor.py:108: DeprecationWarning: scipy.sqrt is deprecated and will be removed in SciPy 2.0.0, use numpy.lib.scimath.sqrt instead
  return sp.sqrt(sp.mean((y_test - y) ** 2))
###rmse=55132006.43, R2=0.95, R22=0.79, clf.score=0.95
'''

plt.grid()
plt.legend(["1", "2", "3", "100"], loc="upper left")
# plt.show()
plt.savefig('i1advanced.png')