import random
import numpy as np

def single_perceptron(x):
    # print('-' * 20 )
    # x = [10, 20, 30, 40, 50]
    print('x=', x)
    w = np.random.rand(1,5)
    threshold = 100
    output = None
    # print('w ->', w, w.shape)
    w = w.T
    print('w ->', w, w.shape)
    isum = np.dot(x, w)
    print('sum=', isum)

    if isum <= threshold:
        output = 0
    else:
        output = 1
    print(output)



def main():
    for i in range(10):
        print('#'*10, i)
        x = np.random.randint(2, size=5) * 10
        single_perceptron(x)


if __name__ == "__main__":
    main()