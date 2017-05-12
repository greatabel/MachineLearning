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


if __name__ == "__main__":
    load_sanders_data()