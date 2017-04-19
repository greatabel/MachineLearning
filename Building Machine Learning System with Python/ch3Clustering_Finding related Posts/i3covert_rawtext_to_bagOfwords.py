from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(min_df=1)
print('dir(vectorizer)=',dir(vectorizer),'\nvectorizer=', vectorizer,'\n')

content = ["How to format my hard disk", "Hard disk format problems "]
X = vectorizer.fit_transform(content)
print('vectorizer.get_feature_names()=',vectorizer.get_feature_names())