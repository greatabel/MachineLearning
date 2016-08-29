import os
import scipy as sp
from termcolor import colored,cprint
import matplotlib.pyplot as plt

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.polyfit.html

sp.random.seed(3)

def error(f, x,y):
    return sp.sum( (f(x) - y)**2 )

data = sp.genfromtxt("data/web_traffic.tsv", delimiter="\t")
print(data[:3])
print(data.shape)

x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

plt.scatter(x,y, s=10)
plt.title("We traffic over the last month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)],
    ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid(True, linestyle='-', color='0.75')
# plt.show()



# create and plot models
fp1, res1, rank1, sv1, rcond1 = sp.polyfit(x, y, 1, full=True)
print('#'*10,fp1, res1, rank1, sv1, rcond1,'#'*10)
print("Model parameters of fp1: %s" % fp1)
print("Error of the model of fp1:", res1)
f1 = sp.poly1d(fp1)
print(colored('error=','red'),error(f1, x, y))

fx = sp.linspace(0,x[-1], 1000) 
# generate X-values for plotting
plt.plot(fx, f1(fx), linewidth=4)
plt.legend(["d=%i" % f1.order], loc="upper left")




# 2次系数
f2p = sp.polyfit(x, y, 2)
print('f2p=',f2p)
f2 = sp.poly1d(f2p)
print(colored('error=','red'),error(f2,x,y))
fx2 = sp.linspace(0,x[-1], 1000) 
# generate X-values for plotting
plt.plot(fx2, f2(fx2), linewidth=4)
plt.legend(["d=%i" % f2.order], loc="upper left")







plt.show()

