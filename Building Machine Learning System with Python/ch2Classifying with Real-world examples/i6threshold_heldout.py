import numpy
from sklearn.datasets import load_iris
from termcolor import colored

from i5threshold import fit_model, accuracy

data = load_iris()
features = data['data']
labels = data['target_names'][data['target']]

print('features:', features)
print('labels:', labels)
print(colored('='*20, 'red'))

# we remove setosa examples as they are too easy:
is_setosa = (labels == 'setosa')
features = features[~is_setosa]
labels = labels[~is_setosa]

print('features:', features)
print('labels:', labels)