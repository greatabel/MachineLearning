import autograd.numpy as np

#  https://zh.wikipedia.org/wiki/%E5%8F%8C%E6%9B%B2%E5%87%BD%E6%95%B0
#  https://docs.scipy.org/doc/numpy/reference/generated/numpy.tanh.html

a = np.tanh((0, np.pi*1j, np.pi*1j/2))
print(a,'#',len(a), '#',a[0])
b = np.tanh((0,-1000000,1000000))
print(b)