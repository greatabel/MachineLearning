import mahotas as mh
import numpy as np
from matplotlib import pyplot as plt

# Load image & convert to B&W
image = mh.imread('AbelSimpleImageDataset/1.jpg')

plt.imshow(image)
# plt.show()

image = image - image.mean()
plt.show()