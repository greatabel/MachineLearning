import numpy as np

def fit_model(k, features, labels):
    return k, features.copy(), labels.copy()


def plurality(xs):
    from collections import defaultdict
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    maxv = max(counts.values())
    for k, v in counts.items():
        if v == maxv:
            return k

# if __name__ == "__main__":
#     a = ['a','b','a','c']
#     print(plurality(a))