# https://cos.name/2010/10/lda_topic_model/

from os import path
from termcolor import colored
import time

from gensim import corpora, models, similarities
from i2wordcloud import create_cloud

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
    # print("ti=", ti)
    # show_topic(topicid, topn=10)
    # Return a list of (word, probability) 2-tuples for the most probable words in topic topicid.

    # Only return 2-tuples for the topn most probable words (ignore the rest).
    words = model.show_topic(ti, 64)
    if ti < 3:
        print('words=', words,len(words))
    tf = sum(w for f, w in words)
    # print('\ntf=', tf)

    with open('temp_topics.txt', 'a+') as output:
        output.write("topicid:" + str(ti)+"\n")
        output.write('\n'.join('{}:{}'.format(w, int(1000. * w / tf)) for f, w in words))
        output.write("\n\n\n")
