import time
import re
start_time = time.time()

import numpy as np
from termcolor import colored

from sklearn.metrics import precision_recall_curve, roc_curve, auc
from sklearn.naive_bayes import MultinomialNB
# from sklearn.cross_validation import ShuffleSplit
from sklearn.model_selection import ShuffleSplit
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from i4utils import load_sanders_data, tweak_labels, plot_pr
from i4utils import load_sent_word_net


sent_word_net = load_sent_word_net()

phase = "03"

emo_repl = {
    # positive emoticons
    "&lt;3": " good ",
    ":d": " good ",  # :D in lower case
    ":dd": " good ",  # :DD in lower case
    "8)": " good ",
    ":-)": " good ",
    ":)": " good ",
    ";)": " good ",
    "(-:": " good ",
    "(:": " good ",

    # negative emoticons:
    ":/": " bad ",
    ":&gt;": " sad ",
    ":')": " sad ",
    ":-(": " bad ",
    ":(": " bad ",
    ":S": " bad ",
    ":-S": " bad ",
}

emo_repl_order = [k for (k_len, k) in reversed(
    sorted([(len(k), k) for k in emo_repl.keys()]))]

re_repl = {
    r"\br\b": "are",
    r"\bu\b": "you",
    r"\bhaha\b": "ha",
    r"\bhahaha\b": "ha",
    r"\bdon't\b": "do not",
    r"\bdoesn't\b": "does not",
    r"\bdidn't\b": "did not",
    r"\bhasn't\b": "has not",
    r"\bhaven't\b": "have not",
    r"\bhadn't\b": "had not",
    r"\bwon't\b": "will not",
    r"\bwouldn't\b": "would not",
    r"\bcan't\b": "can not",
    r"\bcannot\b": "can not",
}

def create_ngram_model():
    # clean 结果比较
    # 0.757   0.046   0.850   0.044   
    # == Pos vs. rest ==
    # 0.595   0.064   0.668   0.071   
    # == Neg vs. rest ==
    # 0.712   0.044   0.505   0.067   
    # time spent: 51.199045181274414


    # 0.757   0.046   0.837   0.051   
    # == Pos vs. rest ==
    # 0.612   0.071   0.670   0.062   
    # == Neg vs. rest ==
    # 0.714   0.045   0.573   0.073   
    # time spent: 5.772912979125977
    def preprocessor(tweet):
        global emoticons_replaced
        tweet = tweet.lower()

        for k in emo_repl_order:
            tweet = tweet.replace(k, emo_repl[k])
        for r, repl in re_repl.items():
            tweet = re.sub(r, repl, tweet)

        return tweet

    tfidf_ngrams = TfidfVectorizer(preprocessor=preprocessor,
                                   analyzer="word")
    clf = MultinomialNB()
    pipeline = Pipeline([('tfidf', tfidf_ngrams), ('clf', clf)])
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
        # fpr, tpr, roc_thresholds = roc_curve(y_test, proba[:, 1])
        precision, recall, pr_thresholds = precision_recall_curve(
            y_test, proba[:, 1])

        pr_scores.append(auc(recall, precision))
        precisions.append(precision)
        recalls.append(recall)
        thresholds.append(pr_thresholds)

    scores_to_sort = pr_scores
    # print('np.argsort(scores_to_sort):', np.argsort(scores_to_sort),len(scores_to_sort) / 2)
    median = np.argsort(scores_to_sort)[int(len(scores_to_sort) / 2)]

    if plot:
        plot_pr(pr_scores[median], name, "01", precisions[median],
                recalls[median], label=name)

        summary = (np.mean(scores), np.std(scores),
                   np.mean(pr_scores), np.std(pr_scores))
        print("%.3f\t%.3f\t%.3f\t%.3f\t" % summary)

    return np.mean(train_errors), np.mean(test_errors)


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
    print("== Pos vs. neg ==")
    # 区分出积极和消极，过滤掉中性
    pos_neg = np.logical_or(Y_orig == "positive", Y_orig == "negative")
    # print(pos_neg)
    X = X_orig[pos_neg]
    Y = Y_orig[pos_neg]
    # print(Y,len(Y), end='\n')
    Y = tweak_labels(Y, ["positive"])
    for i in X[0:5]:
        print( colored("X-> ", 'red'), i, end='\n')

    print('#'*10, '\n', Y, len(Y))
    train_model(create_ngram_model, X, Y, name="pos vs neg", plot=True)
    
    print("== Pos/neg vs. irrelevant/neutral ==")
    X = X_orig
    Y = tweak_labels(Y_orig, ["positive", "negative"])
    train_model(create_ngram_model, X, Y, name="sent vs rest", plot=True)

    print("== Pos vs. rest ==")
    X = X_orig
    Y = tweak_labels(Y_orig, ["positive"])
    train_model(create_ngram_model, X, Y, name="pos vs rest", plot=True)

    print("== Neg vs. rest ==")
    X = X_orig
    Y = tweak_labels(Y_orig, ["negative"])
    train_model(create_ngram_model, X, Y, name="neg vs rest", plot=True)

    print("time spent:", time.time() - start_time)