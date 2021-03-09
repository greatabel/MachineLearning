from sklearn.metrics import r2_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
print(r2_score(y_true, y_pred))  
y_true = [[0.5, 1], [-1, 1], [7, -6]]
y_pred = [[0, 2], [-1, 2], [8, -5]]
print(r2_score(y_true, y_pred,\
        multioutput='variance_weighted'))
y_true = [1,2,3]
y_pred = [1,2,3]
print(r2_score(y_true, y_pred))
y_true = [1,2,3]
y_pred = [2,2,2]
print(r2_score(y_true, y_pred))
y_true = [1,2,3]
y_pred = [3,2,1]
print(r2_score(y_true, y_pred))
