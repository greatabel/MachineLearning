from i8load import load_dataset
import numpy as np

# Import sklearn implementation of KNN
from sklearn.neighbors import KNeighborsClassifier
from termcolor import colored

features, labels = load_dataset('seeds')

# start for test

# features = features[:6]
# labels = labels[:6]

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

    # print(colored('\ntraining,testing:', 'blue'),training,testing,'\n')
    # print('features[training], labels[training]:',features[training], labels[training])
    # print('features[testing]:',features[testing])

    # We learn a model for this fold with `fit` and then apply it to the
    # testing data with `predict`:
    classifier.fit(features[training], labels[training])
    prediction = classifier.predict(features[testing])
    # print('prediction=', prediction)
        # np.mean on an array of booleans returns the fraction of correct decisions
    # for this fold:
    curmean = np.mean(prediction == labels[testing])
    means.append(curmean)
print('Result of cross-validation using KFold: {}'.format(means))





# The function cross_val_score does the same thing as the loop above with a
# single function call

from sklearn.model_selection import cross_val_score
crossed = cross_val_score(classifier, features, labels)
print('Result of cross-validation using cross_val_score: {}'.format(crossed))

# The results above use the features as is, which we learned was not optimal
# except if the features happen to all be in the same scale. We can pre-scale
# the features as explained in the main text:

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
classifier = Pipeline([('norm', StandardScaler()), ('knn', classifier)])
crossed = cross_val_score(classifier, features, labels)
print('Result with prescaling: {}'.format(crossed))



# Now, generate & print a cross-validated confusion matrix for the same result
from sklearn.metrics import confusion_matrix
names = list(set(labels))
labels = np.array([names.index(ell) for ell in labels])
preds = labels.copy()
preds[:] = -1
for train, test in kf.split(features):
    classifier.fit(features[train], labels[train])
    preds[test] = classifier.predict(features[test])

cmat = confusion_matrix(labels, preds)
print()
print('Confusion matrix: [rows represent true outcome, columns predicted outcome]')
print(cmat)