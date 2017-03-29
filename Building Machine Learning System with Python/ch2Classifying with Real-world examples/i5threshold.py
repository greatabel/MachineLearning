import numpy

def fit_model(features, labels):
    best_acc = -1.0
    for fi in range(features.shape[1]):
        thresh = features[:, fi].copy()
        # test all featur value in order
        print('before sort thresh:',thresh)
        thresh.sort()
        print('before sort thresh:',thresh)





def predict(model, features):
    return 0

def accuracy(features, labels, model):
    return 0