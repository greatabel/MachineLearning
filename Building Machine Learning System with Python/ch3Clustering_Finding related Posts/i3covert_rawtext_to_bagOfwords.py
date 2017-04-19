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