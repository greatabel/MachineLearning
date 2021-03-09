import numpy as np

X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] 
                ])
y = np.array([[0,0,1,1]]).T 

print(X, y)

def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

np.random.seed(100)

syn0 = np.random.random((3,1))
print('syn0 ->', syn0)
for i in range(30):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    print('l1 -> ',l1)
    l1_error = y - l1
    print('l1_error -> ', l1_error)
    l1_delta = l1_error * nonlin(l1, True)
    print('l1_delta ->', l1_delta)
    syn0 += np.dot(l0.T, l1_delta)
    print('syn0:', syn0)

target = np.array([[1, 0, 0]])
print(target)
print('target->', nonlin(np.dot(target, syn0)))






