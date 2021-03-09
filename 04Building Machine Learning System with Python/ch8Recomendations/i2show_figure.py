from i0load_ml100k import load
from matplotlib import pyplot as plt


data = load()
plt.gray()
plt.imshow(data[:200, :200], interpolation='nearest')
plt.xlabel('User ID')
plt.ylabel('Film ID')
plt.savefig('charts/Figure_08_03_DataMatrix.png')