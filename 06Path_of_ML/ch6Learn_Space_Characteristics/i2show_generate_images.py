import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


DIR = '../data/moredata/'
img = load_img(DIR + 'dog.png')  # 加载成PIL图片 400*400


fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3) # 2行，每行3张plot
for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
    ax.axis("off") # 关闭坐标轴

# 看几张生成的图片
TITLE_SIZE = 8
ax1.set_title('original', fontsize=TITLE_SIZE)
ax1.imshow(img)
ax2.set_title('slope-crop', fontsize=TITLE_SIZE)
ax2.imshow(load_img(DIR + 'gen_0_863.png'))
ax3.set_title('partial_enlarged', fontsize=TITLE_SIZE)
ax3.imshow(load_img(DIR + 'gen_0_1503.png'))
ax4.set_title('crop-horizontal_flip', fontsize=TITLE_SIZE)
ax4.imshow(load_img(DIR + 'gen_0_1702.png'))
ax5.set_title('slope-crop2', fontsize=TITLE_SIZE)
ax5.imshow(load_img(DIR + 'gen_0_1823.png'))
ax6.set_title('slope-crop-horizontal_flip', fontsize=TITLE_SIZE)
ax6.imshow(load_img(DIR + 'gen_0_2117.png'))
plt.show()