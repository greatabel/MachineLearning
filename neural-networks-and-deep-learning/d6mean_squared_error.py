import numpy as np
from termcolor import colored

def mse(y, y_pred):
    mse = np.mean((y - y_pred)**2)

def generate_test_data():
    a = 2
    b = 3
    x = np.random.randn(10, 1)
    print(x, type(x))
    f = a * x + b
def main():

    print(colored('result =>', 'red'))

if __name__ == "__main__":
    main()