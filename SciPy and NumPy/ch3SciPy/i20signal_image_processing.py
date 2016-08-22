import numpy as np
from scipy.misc import imread, imsave 
from glob import glob

# 我为osx 的python3.5 允许脚本需要： pip3.5 install Pillow

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
imsave('i20space/stacked_image.jpg', im1)
