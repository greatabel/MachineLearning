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
is_setosa = (labels == 'setosa')
# print('is_setosa = ', is_setosa)
max_setosa = plength[is_setosa].max()
min_non_setosa = plength[~is_setosa].min()

print('Maximum of setosa: {0}.'.format(max_setosa))
print('Minimum of others: {0}.'.format(min_non_setosa))

# ----- i4 ----------------
# 找出不是setosa之外的
features = features[~is_setosa]
labels = labels[~is_setosa]

# 创建新的目标
is_virginica = (labels == 'virginica')

# inialize best_acc to impssibly low values
best_acc = -1.0
# print('features=',features)
for fi in range(features.shape[1]):
    # print('fi=',fi)
    # thresh 是第 fi 个向量
    # print(colored('fi '*5+str(fi), 'red'))

    thresh = features[:,fi]

    # print('thresh=', thresh)
    for t in thresh:
        # print('t=', t)
        feature_i = features[:,fi]
        pred = (feature_i > t)
        # print('pred=', pred)
        # print('is_virginica=',is_virginica)
        # print('pred == is_virginica',(pred == is_virginica))
        acc = (pred == is_virginica).mean()
        rev_acc = (pred == ~is_virginica).mean()
        if rev_acc > acc:
            reverse = True
            acc = rev_acc
        else:
            reverse = False

        if acc > best_acc:
            best_acc = acc
            best_fi = fi
            best_t = t
            best_reverse = reverse

print('最好积累值:',best_acc,'第几个:',best_fi,'数值:',best_t ,'是否反转:',best_reverse)
    # print('thresh=',thresh)
