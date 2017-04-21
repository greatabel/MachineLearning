import nltk.stem

s = nltk.stem.SnowballStemmer('english')
print(s.stem('graphics'))