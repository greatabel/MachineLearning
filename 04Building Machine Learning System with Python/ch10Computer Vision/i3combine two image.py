import numpy as np
import mahotas as mh

# This little script just builds an image with two examples, side-by-side:

text = mh.imread("AbelSimpleImageDataset/female1.png")
building = mh.imread("AbelSimpleImageDataset/male1.png")
h, w, _ = text.shape
print(h,w,'here')
canvas = np.zeros((h, 2 * w + 128, 3), np.uint8)
canvas[:, -w:] = building
canvas[:, :w] = text
canvas = canvas[::4, ::4]
mh.imsave('data/figure10.png', canvas)