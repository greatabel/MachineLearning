from sklearn.model_selection import ShuffleSplit
import numpy as np


X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([1, 2, 1, 2])
rs = ShuffleSplit(n_splits=3, test_size=.25, random_state=0)
rs.get_n_splits(X)
print(rs)
ShuffleSplit(n_splits=3, random_state=0, test_size=0.25, train_size=None)
for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)

rs = ShuffleSplit(n_splits=3, train_size=0.5, test_size=.25,
                     random_state=0)

for train_index, test_index in rs.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)