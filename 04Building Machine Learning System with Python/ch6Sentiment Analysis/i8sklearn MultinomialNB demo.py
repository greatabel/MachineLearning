import numpy as np

# http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
# MultinomialNB 假设特征就是出现次数
X = np.random.randint(5, size=(6, 10))
y = np.array([1, 2, 3, 4, 5, 6])
from sklearn.naive_bayes import MultinomialNB

print(X, y, end='\n')
clf = MultinomialNB()
clf.fit(X, y)

print('X[2:3]=', X[2:3])
print(clf.predict(X[2:3]))