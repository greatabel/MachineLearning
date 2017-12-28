# from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets


# mypath = "../../DataSet/MNIST_data/"
# __input = read_data_sets(mypath)
# print("__input.train.images.shape=", __input.train.images.shape)


import numpy as np # 快速操作结构数组的工具
import pandas as pd # 数据分析处理工具
import matplotlib.pyplot as plt # 画图工具
from sklearn import datasets # 机器学习库

#数据集 0-setosa、1-versicolor、2-virginica
scikit_iris = datasets.load_iris()
# 转换成pandas的DataFrame数据格式，方便观察数据
iris = pd.DataFrame(data=np.c_[scikit_iris['data'], scikit_iris['target']],
                     columns=np.append(scikit_iris.feature_names, ['y']))
print('iris.head(2) = ', iris.head(2))
print(iris.isnull().sum())

# 观察样本中按类别数量是否比较均衡
print(iris.groupby('y').count())