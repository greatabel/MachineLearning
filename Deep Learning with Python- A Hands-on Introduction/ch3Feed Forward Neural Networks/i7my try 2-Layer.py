import autograd.numpy as np
import autograd.numpy.random as npr

from termcolor import colored

examples = 4
features = 2
D = (npr.randn(examples, features), npr.randn(examples))
print(colored('输入数据和输出数据 =>', 'red'), D)

