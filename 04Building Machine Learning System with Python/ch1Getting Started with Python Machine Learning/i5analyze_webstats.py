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

print('sp.sum(sp.isnan(y))=',sp.sum(sp.isnan(y)) )
x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]
print(x[:3])
print(y[:3])

import matplotlib.pyplot as plt

plt.scatter(x,y, s=10)
plt.title("We traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
    ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')
plt.show()