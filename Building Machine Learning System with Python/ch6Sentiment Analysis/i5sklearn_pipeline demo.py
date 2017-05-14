# http://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html

from sklearn import svm
from sklearn.datasets import samples_generator
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression
from sklearn.pipeline import Pipeline

# generate some data to play with
X, y = samples_generator.make_classification(
        n_informative=5, n_redundant=0, random_state=42)

# print(X, y,len(X), len(y))
anova_filter = SelectKBest(f_regression, k=5)
clf = svm.SVC(kernel='linear')
anova_svm = Pipeline([('anova', anova_filter), ('svc', clf)])
anova_svm.set_params(anova__k=10, svc__C=.1).fit(X, y)
print(anova_svm.score(X, y)    )
print(anova_svm.named_steps['anova'].get_support())