import numpy as np

x = np.arange(6)
x = x.reshape((2,3))

x_zero =  np.zeros_like(x)
x_empty = np.empty_like(x)
x_one   = np.ones_like(x)


print(x)
print('#'*5, x_zero)
print('#'*10, x_one)
print('#'*10,'return random is:', x_empty)
