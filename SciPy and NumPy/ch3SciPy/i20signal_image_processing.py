import numpy as np
from scipy.misc import imread, imsave 
from glob import glob
# Getting the list of files in the directory 
files = glob('i20space/*.JPG')
print(files)
# Opening up the first image for loop
im1 = imread(files[0]).astype(np.float32)

# Starting loop and continue co-adding new images 
for i in range(1, len(files)):
    print(i)
    im1 += imread(files[i]).astype(np.float32)
# Saving img 
imsave('stacked_image.jpg', im1)
