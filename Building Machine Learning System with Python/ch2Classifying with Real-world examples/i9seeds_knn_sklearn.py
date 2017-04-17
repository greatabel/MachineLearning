from i8load import load_dataset
import numpy as np

# Import sklearn implementation of KNN
from sklearn.neighbors import KNeighborsClassifier

features, labels = load_dataset('seeds')
classifier = KNeighborsClassifier(n_neighbors=4)

n = len(features)
correct = 0.0
for ei in range(n):
    training = np.ones(n, bool)
    training[ei] = 0
    testing = ~training
    classifier.fit(features[training], labels[training])
    pred = classifier.predict(features[ei])
    correct += (pred == labels[ei])
print('Result of leave-one-out: {}'.format(correct/n))
