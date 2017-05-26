try:
    import nltk.corpus
except ImportError:
    print("nltk not found")
    print("please install it")
    raise

from scipy.spatial import distance
import numpy as np
from gensim import corpora, models
import sklearn.datasets
import nltk.stem
from collections import defaultdict
from termcolor import colored
import time
#  如果发现 nltk.corpus.stopwords 找不到：
# import nltk
# nltk.download('stopwords')

english_stemmer = nltk.stem.SnowballStemmer('english')
stopwords = set(nltk.corpus.stopwords.words('english'))
stopwords.update(['from:', 'subject:', 'writes:', 'writes'])

class DirectText(corpora.textcorpus.TextCorpus):
    # def __init__(self, input=None):
    #     print('len(input)=', len(input))
    #     super(corpora.textcorpus.TextCorpus, self).__init__()
    #     self.input = input
    #     # print('self.input=', self.input)
    #     self.dictionary = corpora.Dictionary(input)
    #     self.metadata = False
    #     if input is not None:
    #         self.dictionary.add_documents(input)
    #         # self.dictionary.add_documents(["test","again"])

    #         print('DirectText  len(dictionary)',len(self.dictionary) )
    #     else:
    #         logger.warning("No input document stream provided; assuming "
    #                        "dictionary will be initialized some other way.")

    def get_texts(self):
        # print('here get_texts')
        return self.input

    # def __len__(self):
    #     print('here __len__')
    #     return len(self.input)


try:
    dataset = sklearn.datasets.load_mlcomp("20news-18828", "train",
                                       mlcomp_root='./data')
except:
    print("Newsgroup data not found.")
    print("Please download from http://mlcomp.org/datasets/379")
    print("And expand the zip into the subdirectory data/")
    print()
    print()
    raise


start = time.time()
try:
    dataset = sklearn.datasets.load_mlcomp("20news-18828", "train",
                                       mlcomp_root='./data')
except:
    print("Newsgroup data not found.")
    print("Please download from http://mlcomp.org/datasets/379")
    print("And expand the zip into the subdirectory data/")
    print("The website may need register a user.")
    print()
    raise


# print(dir(dataset),dataset.DESCR, dataset.filenames, dataset.data[0:2],
#     dataset.target[0:2], dataset.target_names[0:2])
otexts = dataset.data
texts = dataset.data
# Damn. to the book 's author :your code is broken in py3. I just fix it.
texts = [t.decode('utf-8', 'ignore') for t in texts]
texts = [t.split() for t in texts]
texts = [list(map(lambda w: w.lower(), t)) for t in texts]
texts = [list(filter(lambda s: not len(set("+-.?!()>@012345689") & set(s)), t))
         for t in texts]
texts = [list(filter(lambda s: (len(s) > 3) and (s not in stopwords), t))
         for t in texts]
texts = [list(map(english_stemmer.stem, t)) for t in texts]
usage = defaultdict(int)
for t in texts:

    for w in set(t):
        usage[w] += 1
limit = len(texts) / 10
# limit = 10

too_common = [w for w in usage if usage[w] > limit]
too_common = set(too_common)
# print('len(too_common)=',len(too_common))
texts = [list(filter(lambda s: s not in too_common, t)) for t in texts]
print(texts[0],'@'*5,texts[1])
print('english_stemmer.stem=', help(english_stemmer.stem))
print('\nlen(texts)=', len(texts),'#'*5, texts[0:2])
# for i in range(2):
#     print(list(texts[i]))
# print('len(texts)=',len(texts))
end = time.time()
print(colored('time:(end - start)=', 'magenta'), (end - start))
start = time.time()


corpus = DirectText(texts)
dictionary = corpus.dictionary
# dictionary = corpora.Dictionary(line.lower().split() for line in texts)
print('#'*10, len(dictionary),len(texts))
try:
    dictionary['computer']
except:
    pass
# print('#'*10, dir(dictionary))
# print('dictionary.id2token=', dictionary.id2token)

model = models.ldamodel.LdaModel(
    corpus, num_topics=100, id2word=dictionary.id2token)

thetas = np.zeros((len(texts), 100))
for i, c in enumerate(corpus):
    for ti, v in model[c]:
        thetas[i, ti] += v

distances = distance.squareform(distance.pdist(thetas))
large = distances.max() + 1
for i in range(len(distances)):
    distances[i, i] = large

print(otexts[1])
print()
print()
print()
print(otexts[distances[1].argmin()])
