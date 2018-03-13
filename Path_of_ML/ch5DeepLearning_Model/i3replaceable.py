import random

d_signals = {
    '视觉信号': '看',
    '听觉信号': '听'
}


class Neuron(object):
    """神经元"""

    def __init__(self, signal_type):
        # 神经元拥有处理某种类型信号的能力
        self.signal_type = signal_type

    def spike(self, x):
        """输入某种类型的刺激信号，有可能激活神经元响应刺激"""
        # 假设神经元有1%的概率被训练
        if random.random() < 0.01:
            self.signal_type = x.signal_type
        if x.signal_type == self.signal_type:
            return d_signals[self.signal_type] + '：' + x.data
        else:
            return d_signals[self.signal_type] + '：' + '什么都没' + \
                   d_signals[self.signal_type] + '到'

from collections import Counter
from i0material_of_brain import SignalInput


class VisualBrain:
    """视觉皮层"""

    def __init__(self, num):
        self.neurons = [Neuron('视觉信号') for i in range(num)]

    def process(self, x):
        """处理信号"""
        print('输入' + x.signal_type + ': ' + x.data)
        reactions = [neuron.spike(x) for neuron in self.neurons]
        # 一群神经元集体响应投票，打印票数最高的响应
        top_reaction = Counter(reactions).most_common(1)
        print('>> 我们用眼睛（视觉皮层） ' + top_reaction[0][0])

class AuditoryBrain:
    """听觉皮层"""
    def __init__(self, num):
        self.neurons = [Neuron('听觉信号') for i in range(num)]

    def process(self, x):
        print('输入' + x.signal_type + '：' + x.data)
        reactions = [neuron.spike(x) for neuron in self.neurons]
        # 一群神经元集体响应投票，打印票数最高的响应
        top_reaction = Counter(reactions).most_common(1)
        print('>> 我在用耳朵（听觉皮层）' + top_reaction[0][0])


class Brain:
    def __init__(self):
        # 分配神经元数量，人脑更依赖视觉输入获得信息，所以视觉神经元数量应该更多
        self.visual_model = VisualBrain(3000)
        self.auditory_model = AuditoryBrain(1000)

    def process(self, x):
        result = {
            '视觉信号': lambda x: self.visual_model.process(x),
            '听觉信号': lambda x: self.auditory_model.process(x),
        }[x.signal_type](x)


if __name__ == "__main__":
    x_see = SignalInput('视觉信号', '一只猫在卖萌!')
    brain = Brain()
    for i in range(100):
        brain.auditory_model.process(x_see)
