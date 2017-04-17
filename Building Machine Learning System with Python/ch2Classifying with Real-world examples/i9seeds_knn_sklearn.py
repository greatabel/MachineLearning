from i8load import load_dataset
import numpy as np

# Import sklearn implementation of KNN
from sklearn.neighbors import KNeighborsClassifier

features, labels = load_dataset('seeds')
classifier = KNeighborsClassifier(n_neighbors=4)

n = len(features)
print('n = len(features) n =', n)

correct = 0.0
for ei in range(n):
    training = np.ones(n, bool)
    print('training=', training)
    training[ei] = 0
    testing = ~training
    print('#training=', training)