from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)
print('dir(vectorizer)=',dir(vectorizer),'\nvectorizer=', vectorizer,'\n')

content = ["How to format my hard disk", "Hard disk format problems "]
X = vectorizer.fit_transform(content)
print('vectorizer.get_feature_names()=',vectorizer.get_feature_names())
print(X.toarray().transpose())

print(colored('*'*25, 'red'))

from i2utils import DATA_DIR
posts = [open(os.path.join(TOY_DIR, f)).read() for f in os.listdir(TOY_DIR)]
X_train = vectorizer.fit_transform(posts)
print('vectorizer.get_feature_names()=',vectorizer.get_feature_names())
print(X.toarray().transpose())
num_samples, num_features = X_train.shape
print("#samples: %d, #featues: %d" %(num_samples, num_features))
