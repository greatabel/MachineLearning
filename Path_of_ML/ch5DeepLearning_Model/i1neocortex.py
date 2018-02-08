from collections import Counter

class VisualBrain:
    """视觉皮层"""

    def __init__(self, num):
        self.neurons = [Neuron('视觉信号') for i in range(num)]

    def process(self, x):
        """处理信号"""
        print('视觉皮层在处理：' + x.data)
