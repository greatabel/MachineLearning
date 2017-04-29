# https://cos.name/2010/10/lda_topic_model/

from os import path
from termcolor import colored
import time

from gensim import corpora, models, similarities, matutils
from i2wordcloud import create_cloud

import matplotlib.pyplot as plt
import numpy as np
from os import path

NUM_TOPICS = 100

# Check that data exists
if not path.exists('./data/ap/ap.dat'):
    print('Error: Expected data to be present at data/ap/')
    print('Please cd into ./data & run ./download_ap.sh')

start = time.time()
# Load the data
corpus = corpora.BleiCorpus('./data/ap/ap.dat',
 './data/ap/vocab.txt')

# Build the topic model
model = models.ldamodel.LdaModel(
    corpus, num_topics=NUM_TOPICS, id2word=corpus.id2word, alpha=None)
num_topics_used = [len(model[doc]) for doc in corpus]


# You can edit the constant below to play around with this parameter
ALPHA = 1.0

model1 = models.ldamodel.LdaModel(
    corpus, num_topics=NUM_TOPICS, id2word=corpus.id2word, alpha=ALPHA)
num_topics_used1 = [len(model1[doc]) for doc in corpus]

end = time.time()
print(colored('time:vectorizer(end - start)=', 'magenta'), (end - start))
start = time.time()


fig,ax = plt.subplots()
ax.hist([num_topics_used, num_topics_used1], np.arange(42))
ax.set_ylabel('Nr of documents')
ax.set_xlabel('Nr of topics')

# The coordinates below were fit by trial and error to look good
ax.text(9, 223, r'default alpha')
ax.text(26, 156, 'alpha=1.0')
fig.tight_layout()
plt.show()

