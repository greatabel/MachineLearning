import numpy as np
from termcolor import colored
import matplotlib.pyplot as plt


def show(s, color="green"):
    show = colored(s, color, attrs=['reverse', 'blink'])
    print(show)

x = np.arange(6)
x = x.reshape((2,3))

x_zero =  np.zeros_like(x)
x_one   = np.ones_like(x)
x_empty = np.empty_like(x)

show('第1部分')
print(x)
print('#'*5, x_zero)
print('#'*10, x_one)
print('#'*15,'return random is:', x_empty)

show('第2部分', 'red')
x = np.arange(-3.0, 6.0, 1)
x_one = np.ones_like(x)
print('@'*3, x)
print('@'*6, x_one)
print('@'*6, 0.2*x_one)
x_vs = np.vstack([x, x_one, 0.2*x_one])
print('@'*9, x_vs)

def softmax(s):
    """softmax函数"""
    return np.exp(s) / np.sum(np.exp(s), axis=0)

show('第3部分', 'yellow')
print('x=', x)
print('*'*5, softmax(x_vs))
print('*'*10, softmax(x_vs).T)

show('第4部分', 'magenta')
plt.plot(x, softmax(x_vs).T, linewidth=2)
plt.show()