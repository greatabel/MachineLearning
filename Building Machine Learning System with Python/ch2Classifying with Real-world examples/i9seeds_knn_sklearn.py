from i8load import load_dataset
import numpy as np

# Import sklearn implementation of KNN
from sklearn.neighbors import KNeighborsClassifier

features, labels = load_dataset('seeds')
# start for test
features = features[:10]
labels = labels[:10]
# end for test

classifier = KNeighborsClassifier(n_neighbors=4)

n = len(features)
correct = 0.0
for ei in range(n):
    training = np.ones(n, bool)
    training[ei] = 0
    testing = ~training
    classifier.fit(features[training], labels[training])
    print('features[ei]=', features[ei])
    # http://stackoverflow.com/questions/35166146/sci-kit-learn-reshape-your-data-either-using-x-reshape-1-1
    temp = np.array(features[ei]).reshape((1, -1))
    pred = classifier.predict(temp)
    correct += (pred == labels[ei])
print('Result of leave-one-out: {}'.format(correct/n))
