from termcolor import colored,cprint
import matplotlib.pyplot as plt

import numpy as np
from scipy.cluster import vq
# Creating data
c1 = np.random.randn(10, 2) + 5 
c2 = np.random.randn(3, 2) - 5 
c3 = np.random.randn(5, 2)

print(c1,colored('c2=','red'),c2,colored('c3=','blue'),c3)
# Pooling all the data into one 180 x 2 array 
data = np.vstack([c1, c2, c3])
print(colored('data =','red'),'\n',data)
# Calculating the cluster centroids and variance 
# from kmeans
centroids, variance = vq.kmeans(data, 3)
# The identified variable contains the information 
# we need to separate the points in clusters
# based on the vq function.
identified, distance = vq.vq(data, centroids)
# Retrieving coordinates for points in each vq # identified core
vqc1 = data[identified == 0]
vqc2 = data[identified == 1]
vqc3 = data[identified == 2]
print('$',vqc1,'#',vqc2,'@',vqc3)