import numpy as np

def score(x, w, b):
    """线性函数"""
    return np.dot(x, w) + b

def sigmoid(s):
    """sigmoid函数"""
    return 1. / (1 + np.exp(-s))

def softmax(s):
    """softmax函数"""
    return np.exp(s) / np.sum(np.exp(s), axis=0)

#--------体验softmax----------
import matplotlib.pyplot as plt
# seaborn是一个matplotlib之上封装统计plot类库，这里我们只是使用seaborn的样式定义

import seaborn as sns
# sns.set_context(rc={'figure.figsize': (14, 7) } )
# sns.set_context("paper")
# sns.set_context("talk")
sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})

x = np.arange(-3.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2*np.ones_like(x)])
plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()