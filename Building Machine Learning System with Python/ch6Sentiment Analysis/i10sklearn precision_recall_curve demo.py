import numpy as np
from sklearn.metrics import precision_recall_curve
from termcolor import colored
# http://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_recall_curve.html
# https://www.zhihu.com/question/19645541


y_true = np.array([0, 0, 1, 1])
y_scores = np.array([0.1, 0.6, 0.3, 0.5])
precision, recall, thresholds = precision_recall_curve(
    y_true, y_scores)

print("precision=", precision) 
print("recall=", recall)
print("thresholds=", thresholds)

# demo 2:
print( colored("<-> " * 15, 'red'))

import numpy.random as r
import pylab
size = 10
y_true = np.array([ 1 if i >= 0.3 else 0 for i in r.random(size) ], dtype=np.float32)
y_pred = r.random(size)
print("y_true=", y_true)
print("y_pred", y_pred)
precision, recall, th = precision_recall_curve(y_true, y_pred)
print("recall=", recall)
print("precision=", precision) 
print("thresholds=", thresholds)
ax = pylab.subplot(2, 1, 2)
ax.plot(recall, precision)
ax.set_ylim([0.0, 1.0])
ax.set_title('Precision recall curve')

pylab.show()