import numpy as np

x = np.arange(6)
x = x.reshape((2,3))

x_zero =  np.zeros_like(x)
x_one   = np.ones_like(x)
x_empty = np.empty_like(x)

print(x)
print('#'*5, x_zero)
print('#'*10, x_one)
print('#'*15,'return random is:', x_empty)

print('-'*20)
x = np.arange(-3.0, 6.0, 1)
x_one = np.ones_like(x)
print('@'*3, x)
print('@'*6, x_one)
print('@'*6, 0.2*x_one)
x_vs = np.vstack([x, x_one, 0.2*x_one])
print('@'*9, x_vs)
