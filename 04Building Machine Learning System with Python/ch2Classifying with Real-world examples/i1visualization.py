from matplotlib import pyplot as plt
import numpy as np

from sklearn.datasets import load_iris
from termcolor import colored


data = load_iris()
print(colored('len(data)=', 'red'),len(data),'type(data)=',type(data))
print('\n '*3, 'data=', data,'\n'*3)

features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names
# setosa = 山鸢尾, versicolor = 变色秋海棠  virginica = 维尔吉妮卡
print(colored('target_names=', 'red'),target_names)
print(colored('len(target)=', 'red'),len(target))
print(colored('len(features)=', 'blue'),len(features),'type(features)=',type(features))
# print(colored('data.DESCR=', 'red'),data.DESCR)
print(' - 萼片sepal length in cm\
        - 萼片sepal width in cm\
        - 花瓣petal length in cm\
        - 花瓣petal width in cm')

for t in range(3):
    if t == 0:
        c = 'r'
        marker = '>'
    elif t == 1:
        c = 'g'
        marker = 'o'
    elif t == 2:
        c = 'b'
        marker = 'x'
    plt.scatter(features[target == t, 0], 
                features[target == t ,1],
                marker=marker,
                c=c)

    # plt.show()