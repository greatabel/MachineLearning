import os
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from common import get_training_data

save_path = "data"

demo_path = "data/train/s/1_右食指_u_b_20210416081253.bmp"


labels = ["n", "s"]
mysize = 130

def cross_validation(dataset):
    X_, y_= list(), list()
    for x, y in dataset:
        X_.append(x)
        y_.append(y)
    return X_, y_

def normalize(X):
    r = np.array(X, dtype=object)
    print('in normalize(X) r=', r,  '#'*20)
    return  r / 255

def reshape(X, y, fig_size):
    X = X.reshape(-1, fig_size[0], fig_size[1], 1)
    y = np.array(y)
    return X, y

def data_argumentation(datagen=None):
    if datagen is None:
        return ImageDataGenerator(
                featurewise_center=False, 
                samplewise_center=False, 
                featurewise_std_normalization=False,  
                samplewise_std_normalization=False, 
                zca_whitening=False,  
                rotation_range = 30) 
    return datagen


def get_model(img_size):
    model = Sequential()
    model.add(Conv2D(32, (3,3), strides=1, padding='same', activation='relu', input_shape=img_size))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2), strides=2, padding='same'))
    model.add(Conv2D(64, (3,3), strides=1, padding='same', activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2), strides=2, padding='same'))
    model.add(Conv2D(64, (3,3), strides=1, padding='same', activation='relu'))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2), strides=2, padding='same'))
    model.add(Conv2D(128, (3,3), strides=1, padding='same', activation='relu'))
    model.add(Dropout(0.2))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2), strides = 2, padding='same'))
    model.add(Flatten())
    model.add(Dense(units=128, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(2, activation='softmax'))
    
    return model

def get_callback():
    callbacks_list = [
            keras.callbacks.ModelCheckpoint(
                filepath='test.h5',
                monitor='val_loss',
                save_best_only=True
            ),
            keras.callbacks.EarlyStopping(
                monitor='val_loss',
                min_delta=0,
                patience=8,
                mode='auto',
                baseline=None,
            )
        ]
    return callbacks_list


train = get_training_data(save_path + "/train")
test = get_training_data(save_path + "/test")
print(f"Train: {len(train)}, Test: {len(test)}")


X_train, y_train = cross_validation(train)
X_test, y_test = cross_validation(test)
X_train = normalize(X_train)
X_test = normalize(X_test)

X_train, y_train = reshape(X_train, y_train, (mysize, mysize))
X_test, y_test = reshape(X_test, y_test, (mysize, mysize))

datagenerator = data_argumentation(None)
datagenerator.fit(X_train)

model = get_model((150, 150, 1))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
print('-'*20)
print(model.summary())

epochs=20
history = model.fit(datagenerator.flow(X_train, y_train, batch_size=32),
                    epochs=epochs, callbacks=get_callback())

history_loss = history.history["loss"]
history_acc = history.history["accuracy"]

plt.plot(history_loss, label="loss")
plt.plot(history_acc, label="acc")
plt.title("Training history")
plt.legend()
plt.show()