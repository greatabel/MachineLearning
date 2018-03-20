import matplotlib.pyplot as plt
from PIL import Image

img_color = Image.open("mnist_color.png") # 原始色彩图
img_gray = img_color.convert('1') # 转换成黑白图

fig, (ax1, ax2) = plt.subplots(1, 2) # 1行，每行2张plot，对比

ax1.axis("off") # 关闭坐标轴
ax2.axis("off")

ax1.set_title('colored')
ax1.imshow(img_color)

ax2.set_title('gray')
ax2.imshow(img_gray)

plt.show()