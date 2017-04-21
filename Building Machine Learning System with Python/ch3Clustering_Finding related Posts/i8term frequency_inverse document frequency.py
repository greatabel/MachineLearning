import nltk.stem

from sklearn.feature_extraction.text import TfidfVectorizer
from termcolor import colored
import os

english_stemmer = nltk.stem.SnowballStemmer('english')

class StemmedTfidfVectorizer(TfidfVectorizer):

    def build_analyzer(self):
        analyzer = super(StemmedTfidfVectorizer, self).build_analyzer()
        return lambda doc: (english_stemmer.stem(w) for w in analyzer(doc))

vectorizer = StemmedTfidfVectorizer(
    min_df=1, stop_words='english', decode_error='ignore')



# --------------following is code copy from i4stop_words.py
from i2utils import DATA_DIR
TOY_DIR = os.path.join(DATA_DIR, "toy")
posts = [open(os.path.join(TOY_DIR, f)).read() for f in os.listdir(TOY_DIR)]
print('posts:', posts)
X_train = vectorizer.fit_transform(posts)

num_samples, num_features = X_train.shape
print("#samples: %d, #featues: %d" %(num_samples, num_features))
print('vectorizer.get_feature_names()=',vectorizer.get_feature_names())

# 向量化
new_post = "imaging databases"
new_post_vec = vectorizer.transform([new_post])
print('new_post_vec =', new_post_vec)
print('new_post_vec.toarray() =',new_post_vec.toarray())



print(colored('*'*25, 'magenta'))
print('计算新帖子和老帖子之间的距离')
import scipy as sp
import sys

# https://zh.wikipedia.org/wiki/%E6%AC%A7%E5%87%A0%E9%87%8C%E5%BE%97%E8%B7%9D%E7%A6%BB
# 欧氏距离
def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

def dist_norm(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())

    delta = v1_normalized - v2_normalized

    return sp.linalg.norm(delta.toarray())

best_doc = None
best_dist = sys.maxsize

# dist = dist_raw
dist = dist_norm

best_i = None

# print('best_dist=', best_dist)
for i in range(0, num_samples):
    post = posts[i]
    # print('post:', post)
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    # print('post_vec=', post_vec)
    d = dist(post_vec, new_post_vec)
    d_raw = dist_raw(post_vec, new_post_vec)
    start = "\033[1m"
    end = "\033[0;0m"
    print("=== Post %i with dist= %s: %s" % (i, start + str(d) + end , post))
    # print("$$$ Post %i with dist_raw = %s: %s" % (i, start + str(d_raw) + end , post))

    if d < best_dist:
        best_dist = d
        best_i = i

print("Best post is %i with dist=%.2f" % (best_i, best_dist))