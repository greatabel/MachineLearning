import time
start_time = time.time()

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from i4utils import load_sanders_data, tweak_labels

if __name__ == "__main__":
    X_orig, Y_orig = load_sanders_data()
    classes = np.unique(Y_orig)
    for c in classes:
        print("#%s: %i" % (c, sum(Y_orig == c)))

    # print(Y_orig)
    # print('@'*30)
    # print( "== Pos vs. neg ==" )
    # print(Y_orig == "positive")
    # print('\n')
    # print(Y_orig == "negative")
    # print('#'*30)

    # 区分出积极和消极，过滤掉中性
    pos_neg = np.logical_or(Y_orig == "positive", Y_orig == "negative")
    # print(pos_neg)
    X = X_orig[pos_neg]
    Y = Y_orig[pos_neg]
    # print(Y,len(Y), end='\n')
    Y = tweak_labels(Y, ["positive"])
    # print(Y, len(Y))