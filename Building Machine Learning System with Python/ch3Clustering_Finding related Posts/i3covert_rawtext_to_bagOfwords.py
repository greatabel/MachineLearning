from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)
print('dir(vectorizer)=',dir(vectorizer))