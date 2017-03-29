import numpy
from sklearn.datasets import load_iris

from i5threshold import fit_model, accuracy

data = load_iris()
features = data['data']
labels = data['target_names'][data['target']]

print('features:', features)
print('labels:', labels)


