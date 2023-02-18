import tensorflow as tf
from tensorflow.keras.utils import plot_model

# Define the shape of the input data
input_shape = (42, 42, 1)  # for example

# Define the number of output classes
num_classes = 10

# Define the first network
input1 = tf.keras.Input(shape=input_shape)
hidden1 = tf.keras.layers.Dense(64, activation='relu')(input1)
hidden2 = tf.keras.layers.Dense(32, activation='relu')(hidden1)
output1 = tf.keras.layers.Dense(num_classes, activation='softmax')(hidden2)
model1 = tf.keras.models.Model(inputs=input1, outputs=output1)

# Define the second network
input2 = tf.keras.Input(shape=input_shape)
hidden3 = tf.keras.layers.Dense(64, activation='relu')(input2)
hidden4 = tf.keras.layers.Dense(32, activation='relu')(hidden3)
output2 = tf.keras.layers.Dense(num_classes, activation='softmax')(hidden4)
model2 = tf.keras.models.Model(inputs=input2, outputs=output2)

# Concatenate the outputs of the two networks
merged = tf.keras.layers.concatenate([output1, output2])

# Define the final output layer
output = tf.keras.layers.Dense(num_classes, activation='softmax')(merged)

# Define the fused model
model = tf.keras.models.Model(inputs=[input1, input2], outputs=output)

# Save the model summary to a PNG image file
plot_model(model, to_file='model_summary.png', show_shapes=True, show_layer_names=True)



'''

                 +-----------+
          +----->|  Hidden 1 |--+
          |      +-----------+  |
          |                     |
    +-----+-----+               |
    |  Network 1 |               |
    +-----------+               |
                                |
          |                     |
          |      +-----------+  |
          +----->|  Hidden 2 |--+
                 +-----------+

                   ||  Concatenate
                   \/

                 +-----------+
          +----->|  Hidden 3 |--+
          |      +-----------+  |
          |                     |
    +-----+-----+               |
    |  Network 2 |               |
    +-----------+               |
                                |
          |                     |
          |      +-----------+  |
          +----->|  Hidden 4 |--+
                 +-----------+

                   ||  Concatenate
                   \/

                 +-----------+
          +----->|  Hidden 5 |--+
          |      +-----------+  |
          |                     |
          |      +-----------+  |
          +----->|  Output   |--+
                 +-----------+
'''
