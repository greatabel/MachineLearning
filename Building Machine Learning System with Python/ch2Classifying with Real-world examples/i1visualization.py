from matplotlib import pyplot as plt
import numpy as np

from sklearn.datasets import load_iris
data = load_iris()
print('len(data)=',len(data))

features = data.data
feature_names = data.feature_names
target = data.target
target_names = data.target_names
print(target_names)