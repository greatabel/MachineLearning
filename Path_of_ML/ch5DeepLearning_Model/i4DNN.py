import numpy as np
np.random.seed(1000)
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils

batch_size = 128 # 梯度下降批数据量
nb_classes = 10 # 类别
epochs = 10 # 循环训练集次数
img_size = 28 * 28 # 输入图片大小

# 加载数据，已执行shuffle-split（训练-测试集随机分割）
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 以Tensorflow为后端，归一化输入数据，生成图片向量
X_train = X_train.reshape(y_train.shape[0], img_size).astype('float32') / 255
X_test = X_test.reshape(y_test.shape[0], img_size).astype('float32') / 255

# One-Hot编码标签，将如[3,2,...] 编码成[[0,0,0,1,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0],...]
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

# 创建模型，增加一层包含128个神经元节点的隐层
model = Sequential([
Dense(128, input_shape=(img_size,), activation='relu'),
Dense(10, input_shape=(128,), activation='softmax'),
])

# 编译模型
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 训练
model.fit(X_train, Y_train,
          batch_size=batch_size, epochs=epochs,
          verbose=1, validation_data=(X_test, Y_test))

# 测试
score = model.evaluate(X_test, Y_test, verbose=0)
print('accuracy: {}'.format(score[1]))