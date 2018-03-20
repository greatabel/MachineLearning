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