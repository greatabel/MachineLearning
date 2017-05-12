import time
start_time = time.time()

import numpy as np

from sklearn.naive_bayes import MultinomialNB
# from sklearn.cross_validation import ShuffleSplit
from sklearn.model_selection import ShuffleSplit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from i4utils import load_sanders_data, tweak_labels


def create_ngram_model():
    tfidf_ngrams = TfidfVectorizer(ngram_range=(1, 3),
                                   analyzer="word", binary=False)
    clf = MultinomialNB()
    pipeline = Pipeline([('vect', tfidf_ngrams), ('clf', clf)])
    return pipeline


def train_model(clf_factory, X, Y, name="NB ngram", plot=False):
    # cv = ShuffleSplit(
    #     n=len(X), n_iter=10, test_size=0.3, indices=True, random_state=0)
    # http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.ShuffleSplit.html
    # old:http://scikit-learn.org/0.15/modules/generated/sklearn
    # .cross_validation.ShuffleSplit.html#sklearn.cross_validation.ShuffleSplit
    cv = ShuffleSplit(
        n_splits=10, test_size=0.3, random_state=0)

    train_errors = []
    test_errors = []

    scores = []
    pr_scores = []
    precisions, recalls, thresholds = [], [], []
    for train, test in cv.split(X):
        X_train, y_train = X[train], Y[train]
        X_test, y_test = X[test], Y[test]

        clf = clf_factory()
        clf.fit(X_train, y_train)

        train_score = clf.score(X_train, y_train)
        test_score = clf.score(X_test, y_test)

        train_errors.append(1 - train_score)
        test_errors.append(1 - test_score)

        scores.append(test_score)
        proba = clf.predict_proba(X_test)
        # print('proba:', proba)


if __name__ == "__main__":
    X_orig, Y_orig = load_sanders_data()
    classes = np.unique(Y_orig)
    for c in classes:
        print("#%s: %i" % (c, sum(Y_orig == c)))

    # print(Y_orig)
    # print('@'*30)
    # print( "== Pos vs. neg ==" )
    # print(Y_orig == "positive")
    # print('\n')
    # print(Y_orig == "negative")
    # print('#'*30)

    # 区分出积极和消极，过滤掉中性
    pos_neg = np.logical_or(Y_orig == "positive", Y_orig == "negative")
    # print(pos_neg)
    X = X_orig[pos_neg]
    Y = Y_orig[pos_neg]
    # print(Y,len(Y), end='\n')
    Y = tweak_labels(Y, ["positive"])
    # print(Y, len(Y))
    train_model(create_ngram_model, X, Y, name="pos vs neg", plot=True)