import numpy as np

def fit_model(k, features, labels):
    return k, features.copy(), labels.copy()


def plurality(xs):
    from collections import defaultdict
    counts = defaultdict(int)
    # print('counts', counts)
    for x in xs:
        counts[x] += 1
        # print('counts['+ x +']=', counts[x])
    maxv = max(counts.values())
    for k, v in counts.items():
        # print('k,v =',k, v)
        if v == maxv:
            return k

# This function was called ``apply_model`` in the first edition
def predict(model, features):
    '''Apply k-nn model'''
    k, train_feats, labels = model
    results = []
    for f in features:
        label_dist = []
        # Compute all distances:
        for t, ell in zip(train_feats, labels):
            label_dist.append((np.linalg.norm(f - t), ell))
        label_dist.sort(key=lambda d_ell: d_ell[0])
        label_dist = label_dist[:k]
        results.append(plurality([ell for _, ell in label_dist]))

    return np.array(results)


def accuracy(features, labels, model):
    preds = predict(model, features)
    return np.mean(preds == labels)

# if __name__ == "__main__":
#     a = ['a','b','a','c','b','c','b']
#     print(plurality(a))