from collections import Counter
from i0material_of_brain import Neuron, SignalInput


class VisualBrain:
    """视觉皮层"""

    def __init__(self, num):
        self.neurons = [Neuron('视觉信号') for i in range(num)]

    def process(self, x):
        """处理信号"""
        print('视觉皮层在处理：' + x.data)

class AuditoryBrain:
    """听觉皮层"""
    def __init__(self, num):
        self.neurons = [Neuron('听觉信号') for i in range(num)]

    def process(self, x):
        print('听觉皮层在处理：' + x.data)


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
    brain = Brain()
    x_see = SignalInput('视觉信号', '一只猫在卖萌!')
    x_hear = SignalInput('听觉信号', '猫咪在喵喵叫!')

    brain.process(x_see)
    brain.process(x_hear)

