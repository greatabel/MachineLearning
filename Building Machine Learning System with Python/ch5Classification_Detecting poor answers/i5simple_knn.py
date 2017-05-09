from sklearn import neighbors


knn = neighbors.KNeighborsClassifier(n_neighbors=2)
print(knn)

knn.fit([[1],[2],[3],[4],[5],[6]],[0,0,0,1,1,1])
print(knn.predict(1.5))
print(knn.predict(37))
print(knn.predict(3))

print(knn.predict_proba(1.5))
print(knn.predict_proba(37))
print(knn.predict_proba(3.5))

