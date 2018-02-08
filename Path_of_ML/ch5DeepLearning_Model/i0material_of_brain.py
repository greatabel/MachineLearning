"""由五感输入的刺激信号。对应行为：看 听 闻 触 嗅"""
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
        """神经元激活函数。输入某种类型的刺激信号，有可能激活神经元响应刺激"""
        if x.signal_type == self.signal_type:
            return d_signals[self.signal_type] + '：' + x.data
        else:
            return d_signals[self.signal_type] + '：' + '什么都没' + \
                   d_signals[self.signal_type] + '到'


class SignalInput(object):
    """输入信号"""
    
    def __init__(self, signal_type, data):
        self.signal_type = signal_type
        self.data = data


x = SignalInput('视觉信号', '一只猫在卖萌!')
print(Neuron('视觉信号').spike(x))
x = SignalInput('听觉信号', '洒水车🎵响起!')
print(Neuron('听觉信号').spike(x))

