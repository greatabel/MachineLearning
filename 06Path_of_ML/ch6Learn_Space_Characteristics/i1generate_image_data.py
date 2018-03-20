from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# 更多API参见官方文档“图片预处理”。https://keras-cn.readthedocs.io/en/latest/preprocessing/image/"""

DIR = '../data/moredata/'

# 随机变形手段的组合
pic_gener = ImageDataGenerator(
    rotation_range=20, # 随机旋转角度范围
    width_shift_range=0.1, # 随机水平移动的范围
    height_shift_range=0.2, # 随机竖直移动的范围
    shear_range=0.2, # 裁剪程度
    zoom_range=0.5, # 随机局部放大的程度
    horizontal_flip=True, # 水平翻转
    fill_mode='nearest') # 当旋转、位移导致图片像素空缺时，填充新像素的方式

img = load_img(DIR + 'dog.png')  # 加载成PIL图片 400*400
x = img_to_array(img)  # 转换成 (400, 400, 3)，第一个数字代表通道数量（RGB颜色通道：3个）
x = x.reshape((1,) + x.shape)  # 转换成Keras/Tensorflow的“tf”格式 (1, 400, 400, 3)第一个数字代表图片数量

i = 0
# 生成随机“变形”的图片；这里可以用flow对单张图片处理，也可以用flow_from_directory对文件夹内所有图片处理
for batch in pic_gener.flow(x, batch_size=1,
                          save_to_dir=DIR[:-1], save_prefix='gen', save_format='png'):
    i += 1
    if i > 30: break # 生成30张