# https://www.youtube.com/watch?v=OAl6eAyP-yo
# https://zh.wikipedia.org/wiki/ROC%E6%9B%B2%E7%BA%BF

# 实际上 书上例子在ch6 的 朴素贝亚斯分类并没有使用 roc_curve 方法，属于定义没有使用的方法
import numpy as np
from sklearn import metrics

y = np.array([1, 1, 2, 2])
print("y=", y)

scores = np.array([0.1, 0.4, 0.35, 0.8])

fpr, tpr, thresholds = metrics.roc_curve(
    y_true=y, y_score=scores, pos_label=2)
print('fpr:', fpr)
print('tpr:', tpr)
print('thresholds:', thresholds)