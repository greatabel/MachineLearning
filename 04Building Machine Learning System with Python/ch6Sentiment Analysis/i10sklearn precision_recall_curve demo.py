import numpy as np
from sklearn.metrics import precision_recall_curve
from termcolor import colored
# http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html
# https://www.zhihu.com/question/19645541
# http://www.cnblogs.com/aquastone/p/random-classifier.html
# http://stackoverflow.com/questions/38165273/sklearn-metrics-precision-recall-curve-why-are-the-precision-and-recall-returne
# http://www.fullstackdevel.com/computer-tec/data-mining-machine-learning/501.html

# y_true = np.array([0, 0, 1, 1])
# y_scores = np.array([0.1, 0.6, 0.3, 0.5])
# precision, recall, thresholds = precision_recall_curve(
#     y_true, y_scores)

# print("precision=", precision) 
# print("recall=", recall)
# print("thresholds=", thresholds)

# demo 2:
print( colored("<-> " * 15, 'red'))

import numpy.random as r
import pylab
size = 10000
y_true = np.array([ 1 if i >= 0.3 else 0 for i in r.random(size) ], dtype=np.float32)
y_pred = r.random(size)
# y_pred1 = []
# for i in range(size):
#     y_pred1.append(0.1)
# print('len(y_pred1)=', len(y_pred1))
# print("y_true=", y_true)
# print("y_pred", y_pred)
precision, recall, th = precision_recall_curve(y_true, y_pred)
# print("recall    (召回率：正例里你的预测覆盖了多少)=", recall)
# print("precision (准确率:你的预测有多少是对的)    =", precision) 

print("thresholds=", th)
ax = pylab.subplot(2, 1, 2)
ax.plot(recall, precision)
ax.set_ylim([0.0, 1.0])
ax.set_title('Precision recall curve')

pylab.show()