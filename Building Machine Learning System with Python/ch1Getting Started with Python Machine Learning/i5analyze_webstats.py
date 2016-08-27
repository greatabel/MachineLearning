import os
import scipy as sp

sp.random.seed(3)

data = sp.genfromtxt("data/web_traffic.tsv", delimiter="\t")
print(data[:3])
print(data.shape)

x = data[:,0]
y = data[:,1]
print('x=', x[:3])
print('y=', y[:3])