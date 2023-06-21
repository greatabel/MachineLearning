import gym
from gym import spaces
import numpy as np
import matplotlib.pyplot as plt

class PowerPlantEnv(gym.Env):
    def __init__(self):
        super(PowerPlantEnv, self).__init__()
        
        # 定义动作和状态空间
        self.action_space = spaces.Discrete(3)  # 三个动作：0, 1, 2
        self.observation_space = spaces.Box(low=0, high=10, shape=(4,), dtype=np.float32)
        self.state = np.random.rand(4) * 10  # 修改为4维

        # 添加一个步数计数器
        self.step_counter = 0

    def step(self, action):
        # 增加步数计数器
        self.step_counter += 1
        
        # 根据动作更新状态
        # 这里只是一个示例，你应该根据你的问题来定义状态更新和奖励机制
        self.state = self.state + np.random.rand(4) - 0.5  # 修改为4维
        
        # 计算奖励
        reward = -np.sum(self.state ** 2)
        
        # 检查是否完成
        done = self.step_counter >= 100  # 假设一个episode最多100步
        
        # 返回新状态，奖励，完成标志和额外信息
        return self.state, reward, done, {}

    def reset(self):
        # 重置环境到初始状态
        self.state = np.random.rand(4) * 10  # 修改为4维
        # 重置步数计数器
        self.step_counter = 0
        return self.state