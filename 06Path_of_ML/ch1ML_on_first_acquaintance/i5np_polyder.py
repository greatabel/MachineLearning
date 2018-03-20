import numpy as np

y = np.poly1d([2, 1, 3])

d_yx = np.polyder(y)
print(d_yx(-7))