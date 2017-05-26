import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# https://matplotlib.org/users/image_tutorial.html
print('images -> numpy arrays')
img = mpimg.imread('data/beatiful.png')
print(img.shape)
print('Plotting numpy arrays as images')
imgplot = plt.imshow(img)
# plt.show()
# imgplot.set_cmap('hot')
plt.colorbar()
plt.show()