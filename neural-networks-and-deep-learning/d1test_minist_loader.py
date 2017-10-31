import i2mnist_loader
import numpy as np
from termcolor import colored


def main():
    training_data, validation_data, test_data = i2mnist_loader.load_data()
    print('type(training_data) ->', type(training_data),len(training_data))
    print('training_data[0][1] ->', training_data[0][1],'training_data[1][1] ->', training_data[1][1])
    print('training_data[0].shape =>', training_data[0].shape)

    print(colored('#'*20 + 'After reshape:', 'red'))
    training_data, validation_data, test_data = i2mnist_loader.load_data_wrapper()
    print('type(training_data) ->', type(training_data))
    training_data = list(training_data)
    print('len(training_data ->', len(training_data))
    print('training_data[0] ->', training_data[0])
    print('type(training_data[0][0]) =>', type(training_data[0][0]),len(training_data[0][0]))
    print('type(training_data[0][1]) =>', type(training_data[0][1]),len(training_data[0][1]))
    
def test_zip():
    print('-'*10,'test_zip','-'*10)
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = zip(a,b)
    d = list(c)
    print(a,b,type(c),d, 'd[0]=',d[0])

if __name__ == "__main__":
    test_zip()
    main()