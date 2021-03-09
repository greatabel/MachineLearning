import numpy as np
from termcolor import colored

def f(x):
    # 函数y = 1*x^2 -2*x + 3
    f = np.poly1d([1, -2, 3])
    return f(x)

def main():
    inputs = np.array([-10, -8, -4, 1, 2, 4, 8, 10])
    for x in inputs:
        print('f('+ str(x) +')=', f(x))

if __name__ == "__main__":
    main()