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
# print('target_names = ', target_names)
# print('target=', target)
# setosa = 山鸢尾, versicolor = 变色秋海棠  virginica = 维尔吉妮卡

# ------- common part -------
labels = target_names[target]
# print('labels=',labels)
# The petal length is the feature at position 2
plength = features[:, 2]

# Build an array of booleans:
is_versicolor= (labels == 'versicolor')
is_virginica= (labels == 'virginica')
# print('is_setosa = ', is_setosa)
max_versicolor = plength[is_versicolor].max()
# min_non_versicolor = plength[~is_versicolor].min()

min_virginica = plength[is_virginica].min()
# min_non_virginica = plength[~is_virginica].min()

print('Maximum of versicolor: {0}.'.format(max_versicolor))
# print('Minimum of others: {0}.'.format(min_non_versicolor))

# print('Maximum of virginica: {0}.'.format(max_virginica))
print('Minimum of virginica: {0}.'.format(min_virginica))

if max_versicolor > min_virginica:
    print('overlap')