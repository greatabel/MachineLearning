from i8load import load_dataset
import numpy as np

# Import sklearn implementation of KNN
from sklearn.neighbors import KNeighborsClassifier
from termcolor import colored

features, labels = load_dataset('seeds')

# start for test

features = features[:5]
labels = labels[:5]

# end for test

# print('features=',features, '\nlabels=', labels,'\n')
classifier = KNeighborsClassifier(n_neighbors=4)

n = len(features)
correct = 0.0
for ei in range(n):
    training = np.ones(n, bool)
    training[ei] = 0
    testing = ~training
    # print('features[training], labels[training]=',features[training], labels[training])
    classifier.fit(features[training], labels[training])

    # http://stackoverflow.com/questions/35166146/sci-kit-learn-reshape-your-data-either-using-x-reshape-1-1
    temp = np.array(features[ei]).reshape((1, -1))
    # print('features[ei]=', colored(temp, 'red'))
    pred = classifier.predict(temp)
    # print('pred=', colored(pred, 'blue'),'labels[ei]=', labels[ei])    
    correct += (pred == labels[ei])
print('Result of leave-one-out: {}'.format(correct/n))


# http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.KFold.html
# Import KFold object
# from sklearn.cross_validation import KFold
from sklearn.model_selection  import KFold

# means will hold the mean for each fold
means = []

# kf is a generator of pairs (training,testing) so that each iteration
# implements a separate fold.
kf = KFold(len(features), random_state=3, shuffle=True)

for training,testing in kf.split(features):
    # We learn a model for this fold with `fit` and then apply it to the
    # testing data with `predict`:
    print(colored('\ntraining,testing:', 'blue'),training,testing,'\n')
    print('features[training], labels[training]:',features[training], labels[training])
    print('features[testing]:',features[testing])
    