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
    

if __name__ == "__main__":
    load_sanders_data()