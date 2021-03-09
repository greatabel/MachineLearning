import numpy as np
from termcolor import colored


a = 2
b = 10

def mse(y, y_pred):
    mse = np.mean((y - y_pred)**2)
    return mse


def generate_test_data(a, b, n):
    x = np.random.randn(n, 1)
    f = a * x + b
    return x, f

def main():
    x, y_pred = generate_test_data(a, b, 10)

    fitting_functions = [ a * x + b, a * x**2 + b, a * x -b]
    for y in fitting_functions:
        print(colored(' mse(y, y_pred) =>', 'red'),  mse(y, y_pred))

if __name__ == "__main__":
    main()