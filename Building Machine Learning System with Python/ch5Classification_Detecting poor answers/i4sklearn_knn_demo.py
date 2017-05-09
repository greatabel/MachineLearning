# http://www.infocool.net/kb/Python/201704/328854.html

#-*-coding:utf-8 -*-
from sklearn import datasets 
#导入内置数据集模块 
from sklearn.neighbors import KNeighborsClassifier 
#导入sklearn.neighbors模块中KNN类
import numpy as np 
np.random.seed(0) 
#设置随机种子，不设置的话默认是按系统时间作为参数，因此每次调用随机模块时产生的随机数都不一样设置后每次产生的一样
iris=datasets.load_iris() 
#导入鸢尾花的数据集，iris是一个类似于结构体的东西，内部有样本数据，如果是监督学习还有标签数据
iris_x=iris.data 
 #样本数据150*4二维数据，代表150个样本，每个样本4个属性分别为花瓣和花萼的长、宽
iris_y=iris.target 
#长150的以为数组，样本数据的标签
indices = np.random.permutation(len(iris_x)) 
#permutation接收一个数作为参数(150),产生一个0-149一维数组，只不过是随机打乱的，当然她也可以接收一个一维数组作为参数，结果是直接对这个数组打乱
iris_x_train = iris_x[indices[:-10]]
 #随机选取140个样本作为训练数据集
iris_y_train = iris_y[indices[:-10]] 
#并且选取这140个样本的标签作为训练数据集的标签
iris_x_test = iris_x[indices[-10:]]
 #剩下的10个样本作为测试数据集
iris_y_test = iris_y[indices[-10:]] 
#并且把剩下10个样本对应标签作为测试数据及的标签

knn = KNeighborsClassifier() 
#定义一个knn分类器对象
knn.fit(iris_x_train, iris_y_train) 
#调用该对象的训练方法，主要接收两个参数：训练数据集及其样本标签

iris_y_predict = knn.predict(iris_x_test) 
 #调用该对象的测试方法，主要接收一个参数：测试数据集
probility=knn.predict_proba(iris_x_test)  
 #计算各测试样本基于概率的预测
neighborpoint=knn.kneighbors(iris_x_test[-1], 5, False)
#计算与最后一个测试样本距离在最近的5个点，返回的是这些样本的序号组成的数组
score=knn.score(iris_x_test,iris_y_test,sample_weight=None)
#调用该对象的打分方法，计算出准确率

print('iris_y_predict = ') 
print(iris_y_predict) 
#输出测试的结果

print('iris_y_test = ')
print(iris_y_test) 
#输出原始测试数据集的正确标签，以方便对比
print('Accuracy:',score )
#输出准确率计算结果
print('neighborpoint of last test sample:',neighborpoint)
 
print('probility:',probility)