import autograd.numpy as np
import autograd.numpy.random as npr

from termcolor import colored

examples = 4
features = 2
D = (npr.randn(examples, features), npr.randn(examples))
print(colored('输入数据和输出数据 =>', 'red'), D)

layer1_units = 2
layers_units = 1
w1 = npr.rand(features, layer1_units)
b1 = npr.rand(layer1_units)
w2 = npr.rand(layer1_units, layers_units)
b2 = 0.0

theta = (w1, b1, w2, b2)
print(colored('theta =>', 'blue'), theta)
