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

end = time.time()
print(colored('time:(end - start)=', 'magenta'), (end - start))
# print(dir(dataset),dataset.DESCR, dataset.filenames, dataset.data[0:2],
#     dataset.target[0:2], dataset.target_names[0:2])
otexts = dataset.data
texts = dataset.data
# print('len(texts)=', len(texts),'#'*5, texts[0:2])
texts = [t.decode('utf-8', 'ignore') for t in texts]
# print('\nlen(texts)=', len(texts),'#'*5, texts[0:2])
texts = [t.split() for t in texts]
texts = [map(lambda w: w.lower(), t) for t in texts]
texts = [filter(lambda s: not len(set("+-.?!()>@012345689") & set(s)), t)
         for t in texts]
texts = [filter(lambda s: (len(s) > 3) and (s not in stopwords), t)
         for t in texts]
texts = [map(english_stemmer.stem, t) for t in texts]
# print('english_stemmer.stem=', help(english_stemmer.stem))
# print('\nlen(texts)=', len(texts),'#'*5, texts[0:2])
# for i in range(2):
#     print(list(texts[i]))

