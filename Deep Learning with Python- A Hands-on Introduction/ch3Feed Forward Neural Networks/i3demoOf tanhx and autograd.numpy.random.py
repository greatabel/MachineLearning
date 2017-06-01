import autograd.numpy as np
import autograd.numpy.random as npr
#  https://zh.wikipedia.org/wiki/%E5%8F%8C%E6%9B%B2%E5%87%BD%E6%95%B0
#  https://docs.scipy.org/doc/numpy/reference/generated/numpy.tanh.html

a = np.tanh((0, np.pi*1j, np.pi*1j/2))
print(a,'#',len(a), '#',a[0])
b = np.tanh((0,-1000000,1000000))
print(b)

print('autograd.numpy.random')
n = npr.rand()
print(n)
n1 =npr.rand(10)
print(n1)
n2 =npr.rand(10, 2)
print(n2)

print('before numpy.random.seed(100)')
c = np.random.rand(4)
print(c)
c = np.random.rand(4)
print(c)
c = np.random.rand(4)
print(c)

np.random.seed(100)
print('after np.random.seed(100)')
c = np.random.rand(4)
print(c)
np.random.seed(100)
c = np.random.rand(4)
print(c)
np.random.seed(100)
c = np.random.rand(4)
print(c)