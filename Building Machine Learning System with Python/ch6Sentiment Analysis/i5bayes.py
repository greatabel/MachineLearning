import time
start_time = time.time()

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from i4utils import load_sanders_data

if __name__ == "__main__":
    X_orig, Y_orig = load_sanders_data()
    classes = np.unique(Y_orig)
    for c in classes:
        print("#%s: %i" % (c, sum(Y_orig == c)))