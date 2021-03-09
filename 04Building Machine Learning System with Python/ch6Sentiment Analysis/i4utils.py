import os
import collections
import csv
import json

from matplotlib import pylab
import numpy as np


DATA_DIR = "data"
CHART_DIR = "charts"

if not os.path.exists(DATA_DIR):
    raise RuntimeError("Expecting directory 'data' in current path")

if not os.path.exists(CHART_DIR):
    os.mkdir(CHART_DIR)

# 把文字或者其他描述性信息 根据条件变成 整形编码
def tweak_labels(Y, pos_sent_list):
    # print('pos_sent_list[0]=', pos_sent_list[0])
    pos = Y == pos_sent_list[0]
    # print('pos=', pos)
    # print('pos_sent_list[1:]=', pos_sent_list[1:])
    for sent_label in pos_sent_list[1:]:
        pos |= Y == sent_label

    Y = np.zeros(Y.shape[0])
    Y[pos] = 1
    # print('before=',Y)
    Y = Y.astype(int)
    # print(Y)

    return Y

def load_sanders_data(dirname=".", line_count=-1):
    count = 0

    topics = []
    labels = []
    tweets = []

    with open(os.path.join(DATA_DIR, dirname, "corpus.csv"), "r") as csvfile:
        metareader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in metareader:
            count += 1
            if line_count > 0 and count > line_count:
                break
            # print(line)
            topic, label, tweet_id = line

            tweet_fn = os.path.join(
                DATA_DIR, dirname, 'rawdata', '%s.json' %tweet_id)
            try:
                tweet = json.load(open(tweet_fn, "r"))
            except IOError:
                # print("Tweet '%s' not found. Skip" %tweet_fn)
                continue

            if 'text' in tweet and tweet['user']['lang'] == "en":
                topics.append(topic)
                labels.append(label)
                tweets.append(tweet['text'])
    # print(topic,'#'*10, labels, '@'*10, tweets)
    tweets = np.asarray(tweets)
    labels = np.asarray(labels)
    # print(tweets, '#'*20, labels)
    return tweets, labels

def plot_pr(auc_score, name, phase, precision, recall, label=None):
    pylab.clf()
    pylab.figure(num=None, figsize=(5, 4))
    pylab.grid(True)
    pylab.fill_between(recall, precision, alpha=0.5)
    pylab.plot(recall, precision, lw=1)
    pylab.xlim([0.0, 1.0])
    pylab.ylim([0.0, 1.0])
    pylab.xlabel('Recall')
    pylab.ylabel('Precision')
    pylab.title('P/R curve (AUC=%0.2f) / %s' % (auc_score, label))
    filename = name.replace(" ", "_")
    pylab.savefig(os.path.join(CHART_DIR, "pr_%s_%s.png" %
                  (filename, phase)), bbox_inches="tight")
    

def load_sent_word_net():

    sent_scores = collections.defaultdict(list)

    with open(os.path.join(DATA_DIR, "SentiWordNet_3.0.0_20130122.txt"), "r") as csvfile:
        reader = csv.reader(csvfile, delimiter='\t', quotechar='"')
        for line in reader:
            if line[0].startswith("#"):
                continue
            if len(line) == 1:
                continue

            POS, ID, PosScore, NegScore, SynsetTerms, Gloss = line
            if len(POS) == 0 or len(ID) == 0:
                continue
            # print POS,PosScore,NegScore,SynsetTerms
            for term in SynsetTerms.split(" "):
                # drop #number at the end of every term
                term = term.split("#")[0]
                term = term.replace("-", " ").replace("_", " ")
                key = "%s/%s" % (POS, term.split("#")[0])
                sent_scores[key].append((float(PosScore), float(NegScore)))
    for key, value in sent_scores.items():
        sent_scores[key] = np.mean(value, axis=0)

    return sent_scores

def log_false_positives(clf, X, y, name):
    with open(os.path.join(DATA_DIR,"FP_" + name.replace(" ", "_") + ".tsv"), "w") as f:
        false_positive = clf.predict(X) != y
        for tweet, false_class in zip(X[false_positive], y[false_positive]):
            f.write("%s\t%s\n" %
                    (false_class, tweet.encode("ascii", "ignore")))

# if __name__ == "__main__":
    # load_sanders_data()
    # word_data = load_sent_word_net()
    # print(len(word_data))
