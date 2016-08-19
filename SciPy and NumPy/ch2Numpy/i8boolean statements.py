from termcolor import colored,cprint
import numpy as np

# https://pypi.python.org/pypi/termcolor

print(colored('# Creating an array','magenta'))
cprint('Creating an array', 'green', 'on_red')

# Creating an image
img1 = np.zeros((20, 20)) + 3 
img1[4:-4, 4:-4] = 6 
img1[7:-7, 7:-7] = 9
print('img1=', img1)
# See Plot A
# Let's filter out all values larger than 2 and less than 6. 
index1 = img1 > 2
index2 = img1 < 6
compound_index = index1 & index2
# The compound statement can alternatively be written as compound_index = (img1 > 3) & (img1 < 7)
img2 = np.copy(img1)
img2[compound_index] = 0
print('img2=', img2)

# See Plot B.
# Making the boolean arrays even more complex 
index3 = img1 == 9
index4 = (index1 & index2) | index3
img3 = np.copy(img1)
img3[index4] = 0 # See Plot C.

# from PIL import Image
# img = Image.fromarray(img1, 'RGB')
# img.save('my.png')
# img.show()
from matplotlib import pyplot as plt
plt.imshow(img1, interpolation='nearest')
plt.show()
plt.imshow(img2, interpolation='nearest')
plt.show()
plt.imshow(img3, interpolation='nearest')
plt.show()