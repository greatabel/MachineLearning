import numpy as np
from termcolor import colored

def fit_model(features, labels):
    best_acc = -1.0
    for fi in range(features.shape[1]):
        thresh = features[:, fi].copy()
        # test all featur value in order
        print(colored('-'*20, 'red'))
        print('before sort thresh:',thresh)
        thresh.sort()
        print('before sort thresh:',thresh)

        for t in thresh:
            pred = (features[:, fi] > t)

            # measure accuray of this
            accuracy = (pred == labels).mean()

            rev_acc = (pred == ~labels).mean()

            if rev_acc > accuracy:
                accuracy = rev_acc
                reverse = True
            else:
                reverse = False

            if accuracy > best_acc:
                best_acc = accuracy
                best_fi = fi
                best_t = t
                best_reverse = reverse
    return best_t, best_fi, best_reverse





def predict(model, features):
    # apply model
    t, fi, reverse = model
    if reverse:
        return features[:, fi] <= t
    else:
        return features[:, fi] > t


def accuracy(features, labels, model):
    preds = predict(model, features)
    return np.mean(preds == labels)