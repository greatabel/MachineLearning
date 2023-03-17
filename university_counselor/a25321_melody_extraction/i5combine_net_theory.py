import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, Flatten, Dense, Reshape, Conv2DTranspose
from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model


# Second Neural Network to convert voice to MIDI
input1 = Input(shape=(100,100,1))
x1 = Conv2D(32, (3,3), activation='relu', padding='same')(input1)
x1 = Conv2D(64, (3,3), activation='relu', padding='same')(x1)
x1 = Flatten()(x1)
output1 = Dense(128, activation='relu')(x1)
m2 = Model(input1, output1)




# First Neural Network to separate human voice
input2 = Input(shape=(128,))
x2 = Dense(256, activation='relu')(input2)
x2 = Reshape((8,8,4))(x2)
x2 = Conv2DTranspose(64, (3,3), strides=2, activation='relu', padding='same')(x2)
output2 = Conv2DTranspose(1, (3,3), strides=2, activation='sigmoid', padding='same')(x2)
m1 = Model(input2, output2)

# Combine both models
combined_model = Model(inputs=m2.input, outputs=m1(m2.output))
plot_model(combined_model, to_file='i5combined_model.png', show_shapes=True)
