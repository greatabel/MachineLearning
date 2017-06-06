import numpy as np

'''
http://iamtrask.github.io/2015/07/12/basic-python-network/
https://medium.com/technology-invention-and-more/how-to-build-a-simple-neural-network-in-9-lines-of-python-code-cc8f23647ca1
https://yjango.gitbooks.io/superorganism/content/ren_gong_shen_jing_wang_luo.html
'''

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

# print('nonlin-->\n')
# print(nonlin(-4.6))
# print(nonlin(4.8))
# print(nonlin(5))
# print(nonlin(-4.8))
# print(nonlin(9.6))
# input dataset

X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] 
                ])

# output dataset           
y = np.array([[0,0,1,1]]).T 

# seed random numbers to make calculation

# deterministic (just a good practice)

np.random.seed(1)
# initialize weights randomly with mean 0

syn0 = 2*np.random.random((3,1)) - 1
 

for iter in range(3):
    # forward propagation
    l0 = X
    l1 = nonlin(np.dot(l0,syn0))   
    # how much did we miss?
    l1_error = y - l1
    # print('l1_error:', l1_error)
    # print('nonlin(l1,True):', nonlin(l1,True))
    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)
    # print('l1_delta:', l1_delta)
    # print('np.dot(l0.T,l1_delta):', np.dot(l0.T,l1_delta) )
    # update weights
    syn0 += np.dot(l0.T,l1_delta) 

print("Output After Training:\n",
     l1,"\nsyn0:", syn0)

