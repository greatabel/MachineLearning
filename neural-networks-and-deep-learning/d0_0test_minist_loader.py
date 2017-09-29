import i2mnist_loader
import numpy as np


def main():
    training_data, validation_data, test_data = i2mnist_loader.load_data()
    print('type(training_data) ->', type(training_data),len(training_data))
    print('training_data[0][1] ->', training_data[0][1],'training_data[1][1] ->', training_data[1][1])
    
def test_zip():
    print('-'*10,'test_zip','-'*10)
    a = [1,2,3,4]
    b = [5,6,7,8]
    c = zip(a,b)
    print(a,b,type(c),list(c))

if __name__ == "__main__":
    test_zip()
    main()