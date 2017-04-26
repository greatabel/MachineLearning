# https://cos.name/2010/10/lda_topic_model/

from gensim import corpora, models, similarities

NUM_TOPICS = 100
# Load the data
corpus = corpora.BleiCorpus('./data/ap/ap.dat',
 './data/ap/vocab.txt')

# Build the topic model
model = models.ldamodel.LdaModel(
    corpus, num_topics=NUM_TOPICS, id2word=corpus.id2word, alpha=None)