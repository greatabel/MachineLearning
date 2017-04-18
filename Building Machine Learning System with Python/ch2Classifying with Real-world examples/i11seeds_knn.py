from i8load import load_dataset
import numpy as np
from i10knn import fit_model, accuracy

features, labels = load_dataset('seeds')

# start for test

features = features[:10]
labels = labels[:10]

# end for test

def cross_validate(features, labels):
    '''Compute cross-validation errors'''
    error = 0.0
    for fold in range(10):
        training = np.ones(len(features), bool)
        training[fold::10] = 0
        testing = ~training
        model = fit_model(1, features[training], labels[training])
        test_error = accuracy(features[testing], labels[testing], model)
        error += test_error

    return error / 10.0

error = cross_validate(features, labels)