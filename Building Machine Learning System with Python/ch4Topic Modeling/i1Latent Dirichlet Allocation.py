# https://cos.name/2010/10/lda_topic_model/

from os import path
from termcolor import colored
import time

from gensim import corpora, models, similarities

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

end = time.time()
print(colored('time:vectorizer(end - start)=', 'magenta'), (end - start))
start = time.time()
# Iterate over all the topics in the model
for ti in range(model.num_topics):
    words = model.show_topic(ti, 64)
    tf = sum(w for f, w in words)
    with open('temp_topics.txt', 'w') as output:
        output.write('\n'.join('{}:{}'.format(w, int(1000. * w / tf)) for f, w in words))
        output.write("\n\n\n")
