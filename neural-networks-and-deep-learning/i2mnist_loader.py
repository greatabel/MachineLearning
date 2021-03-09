import pickle
import gzip

import numpy as np

def load_data():
    f = gzip.open('mnist.pkl.gz', 'rb')
    training_data, validation_data, test_data = pickle.load(f, encoding="latin1")
    f.close()
    return (training_data, validation_data, test_data)


def load_data_wrapper():
    tr_d, va_d, te_d = load_data()

    # print('-'*20, len(tr_d[0]), len(tr_d[1]))
    # print('*'*20, len(va_d[0]), len(va_d[1]))
    # print('@'*20, len(te_d[0]), len(te_d[1]))
    # print(tr_d[0][0],'\n', len(tr_d[0][0]),'^-^'*10, tr_d[1][0])

    training_inputs = [np.reshape(x, (784, 1)) for x in tr_d[0]]
    # print(training_inputs[0],'\n','*'*20, len(training_inputs[0]))
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    # print('##type(training_data)->',type(training_data))
    validation_inputs = [np.reshape(x, (784, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (784, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

def vectorized_result(j):
    """Return a 10-dimensional unit vector with a 1.0 in the jth
    position and zeroes elsewhere.  This is used to convert a digit
    (0...9) into a corresponding desired output from the neural
    network."""
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e

# if __name__ == "__main__":
#     load_data_wrapper()