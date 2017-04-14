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


error = 0.0
for ei in range(len(features)):
    # print('ei-->', ei)
    # choose all position without ei
    training = np.ones(len(features),bool)
    training[ei] = False
    testing = ~training

# # Split the data in two: testing and training
# testing = np.tile([True, False], 50) # testing = [True,False,True,False,True,False...]
# # print('testing=',testing,len(testing))

# # Training is the negation of testing: i.e., datapoints not used for testing,
# # will be used for training
# training = ~testing
# print('traing=', training,len(training))
    print('len(features[training]):',len(features[training]))

    model = fit_model(features[training], is_virginica[training])
    print('model:', model)

    train_accuracy = accuracy(features[training], is_virginica[training], model)
    test_accuracy = accuracy(features[testing], is_virginica[testing], model)

    print('''\
    Training accuracy was {0:.1%}.
    Testing accuracy was {1:.1%} (N = {2}).
    '''.format(train_accuracy, test_accuracy, testing.sum()))
    error += np.sum(test_accuracy != is_virginica[testing])
print('error=', error)
