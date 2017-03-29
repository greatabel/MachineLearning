import numpy as np
from sklearn.datasets import load_iris
from termcolor import colored

from i5threshold import fit_model, accuracy

data = load_iris()
features = data['data']
labels = data['target_names'][data['target']]

# print('features:', features)
print('len(features)=',len(features))
print('labels:', labels)
print(colored('='*20, 'red'))

# we remove setosa examples as they are too easy:
is_setosa = (labels == 'setosa')
features = features[~is_setosa]
labels = labels[~is_setosa]

# print('features:', features)
print('labels:', labels)
print('len(features)=',len(features))

# Now we classify virginica vs non-virginica
is_virginica = (labels == 'virginica')

# Split the data in two: testing and training
testing = np.tile([True, False], 50) # testing = [True,False,True,False,True,False...]
# print('testing=',testing,len(testing))

# Training is the negation of testing: i.e., datapoints not used for testing,
# will be used for training
training = ~testing
# print('traing=', training,len(training))
print('len(features[training]):',len(features[training]))

model = fit_model(features[training], is_virginica[training])
print('model:', model)