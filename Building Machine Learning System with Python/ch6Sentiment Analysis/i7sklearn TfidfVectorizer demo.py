from sklearn.feature_extraction.text import TfidfVectorizer
# http://stackoverflow.com/questions/23792781/
#  tf-idf-feature-weights-using-sklearn-feature-extraction-text-tfidfvectorizer

# http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
corpus = ["This is very strange",
          "This is very nice",
          "This is a flower"]
vectorizer = TfidfVectorizer(min_df=1, ngram_range=(1, 3))
X = vectorizer.fit_transform(corpus)
idf = vectorizer.idf_
d= dict(zip(vectorizer.get_feature_names(), idf)) 
for key in d:
    print("{} = {}".format(key, d[key]))
