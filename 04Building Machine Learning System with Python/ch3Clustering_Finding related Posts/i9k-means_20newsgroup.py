# K-means演示:  https://www.youtube.com/watch?v=_aWzGGNrcic

import sklearn.datasets
import scipy as sp
from termcolor import colored
import time


print('sklearn.datasets.get_data_home()=', sklearn.datasets.get_data_home())

all_data = sklearn.datasets.fetch_20newsgroups(subset="all")
print("Number of total posts: %i" % len(all_data.filenames))
print(all_data.filenames[0:3])

print(colored('*'*25, 'magenta'),'target_names')
print(all_data.target_names, '\n'*3)

#  选取一些新闻组进行 训练
groups = [
    'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware',
    'comp.sys.mac.hardware', 'comp.windows.x', 'sci.space']
train_data = sklearn.datasets.fetch_20newsgroups(subset="train",
                                                 categories=groups)
print("Number of training posts in tech groups:", len(train_data.filenames))


labels = train_data.target
num_clusters = 50  # sp.unique(labels).shape[0]

import nltk.stem
english_stemmer = nltk.stem.SnowballStemmer('english')

from sklearn.feature_extraction.text import TfidfVectorizer


class StemmedTfidfVectorizer(TfidfVectorizer):

    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(min_df=10, max_df=0.5,
                                    stop_words='english', decode_error='ignore'
                                    )


for i in range(0,3):
    print(train_data.data[i],'-'*20,i,'-'*20,'\n')

start = time.time()
vectorized = vectorizer.fit_transform(train_data.data)
num_samples, num_features = vectorized.shape
print("#samples: %d, #features: %d" % (num_samples, num_features))

end = time.time()
print(colored('time:vectorizer(end - start)=', 'magenta'), (end - start))
start = time.time()
# print('vectorizer.get_feature_names()=',vectorizer.get_feature_names())

from sklearn.cluster import KMeans

km = KMeans(n_clusters=num_clusters, n_init=1, verbose=1, random_state=3)
clustered = km.fit(vectorized)

print("km.labels_=%s" % km.labels_)
print("km.labels_.shape=%s" % km.labels_.shape)
print("km.cluster_centers_=%s" % km.cluster_centers_)

from sklearn import metrics
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
# Homogeneity: 0.400
print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
# Completeness: 0.206
print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))
# V-measure: 0.272
print("Adjusted Rand Index: %0.3f" %
      metrics.adjusted_rand_score(labels, km.labels_))
# Adjusted Rand Index: 0.064
print("Adjusted Mutual Information: %0.3f" %
      metrics.adjusted_mutual_info_score(labels, km.labels_))
# Adjusted Mutual Information: 0.197
print(("Silhouette Coefficient: %0.3f" %
       metrics.silhouette_score(vectorized, labels, sample_size=1000)))

end = time.time()
print(colored('time:cluster(end - start)=', 'magenta'), (end - start))