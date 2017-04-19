from sklearn.feature_extraction.text import CountVectorizer
from termcolor import colored
import os


vectorizer = CountVectorizer(min_df=1)
print('dir(vectorizer)=',dir(vectorizer),'\nvectorizer=', vectorizer,'\n')

content = ["How to format my hard disk", "Hard disk format problems "]
X = vectorizer.fit_transform(content)
print('vectorizer.get_feature_names()=',vectorizer.get_feature_names())
print(X.toarray().transpose())


print(colored('*'*25, 'red'))



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

best_doc = None
best_dist = sys.maxsize
dist = dist_raw
# print('best_dist=', best_dist)
for i in range(0, num_samples):
    post = posts[i]
    # print('post:', post)
    if post == new_post:
        continue
    post_vec = X_train.getrow(i)
    # print('post_vec=', post_vec)
    d = dist(post_vec, new_post_vec)
    print("=== Post %i with dist= %.2f: %s" % (i, d, post))

