from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np

# Constructing a random array with 1000 elements 

x = np.random.randn(3) * 100
print( colored( ('x = np.random.randn(3) x=',x),'green') )
print( colored( 'meam(X)：当X为向量，返回向量的均值；当X为矩阵，返回矩阵的每列元素均值构成的行向量。\n'+
    'std样本标准差 \n'+' var 样本方差','blue') )
# Calculating several of the built-in methods # that numpy.array has
mean = x.mean()
std = x.std()
var = x.var()
print('mean=',mean,'std=',std,'var=',var)