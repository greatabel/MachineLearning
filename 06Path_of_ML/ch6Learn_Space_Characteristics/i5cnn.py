from keras.layers import MaxPooling2D, Dropout, Flatten
from keras.models import Sequential
from keras.layers import Convolution2D, Activation

# 套路：卷积-激活-池化
model = Sequential([
Convolution2D(32, 3, 3, input_shape=(128, 128, 3), activation='relu'),
MaxPooling2D(pool_size=(2, 2)),
Convolution2D(64, 3, 3, activation='relu'),
MaxPooling2D(pool_size=(2, 2)),
Flatten(),
])

from keras.layers import Dense

# 追加DNN层
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

import os
import shutil
import random

# 从https://www.kaggle.com/c/dogs-vs-cats/data下载完整的样本集train.zip，解压到下面的目录
train = '../data/dog_cat/train/' 

dogs = [train + i for i in os.listdir(train) if 'dog' in i]
cats = [train + i for i in os.listdir(train) if 'cat' in i]
print('dogs count:' + str(len(dogs)))
print('cats count:' + str(len(cats)))

target = '../data/dog_cat/arrange/' # 目标训练集地址

# 随机化
random.shuffle(dogs)
random.shuffle(cats)

def ensure_dir(dir_path):
    if not os.path.exists(dir_path):
        try:
            os.makedirs(dir_path)
        except OSError:
            pass

# 生成文件夹
ensure_dir(target + 'train/dog')
ensure_dir(target + 'train/cat')
ensure_dir(target + 'validation/dog')
ensure_dir(target + 'validation/cat')

# 复制图片
for dog_file, cat_file in list(zip(dogs, cats))[:5]:
    shutil.copyfile(dog_file, target + 'train/dog/' + os.path.basename(dog_file))
    shutil.copyfile(cat_file, target + 'train/cat/' + os.path.basename(cat_file))

for dog_file, cat_file in list(zip(dogs, cats))[5:10]:
    shutil.copyfile(dog_file, target + 'validation/dog/' + os.path.basename(dog_file))
    shutil.copyfile(cat_file, target + 'validation/cat/' + os.path.basename(cat_file))


from keras.preprocessing.image import ImageDataGenerator

# 图片尺寸
img_width, img_height = 128, 128
input_shape = (img_width, img_height, 3)

train_data_dir = target + 'train'
validation_data_dir = target + 'validation'

# 生成变形图片
train_pic_gen = ImageDataGenerator(
        rescale=1./255, # 对输入图片归一化到0-1区间
        rotation_range=20, 
        width_shift_range=0.2, 
        height_shift_range=0.2, 
        shear_range=0.2, 
        zoom_range=0.5, 
        horizontal_flip=True, # 水平翻转
        fill_mode='nearest')

# 测试集不做变形处理，只需要归一化。关于为什么要做归一化，参见1.4 逻辑分类II：线性分类模型-去均值和归一化
validation_pic_gen = ImageDataGenerator(rescale=1./255)


# 按文件夹生成训练集流和标签，binary：二分类
train_flow = train_pic_gen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary')

# 按文件夹生成测试集流和标签
validation_flow = validation_pic_gen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        batch_size=32,
        class_mode='binary')

from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense

steps_per_epoch = 20
validation_steps = 10
#epochs = 1
epochs = 5 # 循环50轮

# 两层卷积-池化，提取64个平面特征
model = Sequential([
Convolution2D(32, (3, 3), input_shape=input_shape, activation='relu'),
MaxPooling2D(pool_size=(2, 2)),
Convolution2D(64, (3, 3), activation='relu'),
MaxPooling2D(pool_size=(2, 2)),
Flatten(),
Dense(64, activation='relu'),
Dropout(0.5),
Dense(1, activation='sigmoid'),
])

# 损失函数设置为二分类交叉熵
model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit_generator(
        train_flow,
        steps_per_epoch=steps_per_epoch,
        epochs=epochs,
        validation_data=validation_flow,
        validation_steps=validation_steps)

ensure_dir(target + 'weights')
model.save_weights(target + 'weights/' + '1.h5')
