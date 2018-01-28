import numpy as np
from termcolor import colored
import matplotlib.pyplot as plt


def show(s, color="green"):
    show = colored(s, color, attrs=['reverse', 'blink'])
    print(show)

def softmax(s):
    """softmax函数"""
    return np.exp(s) / np.sum(np.exp(s), axis=0)

scores = np.array([0.1, 1, 2])
show('scores数值')
print(scores, scores * 100, scores / 100)
show('softmax(scores), softmax(scores * 100), softmax(scores / 100) ->', 'red')
print(softmax(scores), softmax(scores * 100), softmax(scores / 100))
show('对于softmax函数：概率值大的越大，小的越小','cyan')