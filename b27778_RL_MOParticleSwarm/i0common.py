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
        # 
        self.step_counter += 1

        # 更新状态
        self.state = self.state + np.random.rand(4) - 0.5  # just a placeholder for real state transition function

        # 约束条件
        lower_limit, upper_limit = 1, 9  # replace with your real limits
        self.state[0] = np.clip(self.state[0], lower_limit, upper_limit)

        # 计算奖励
        thermal_cost = self.state[0]  
        carbon_cost = self.state[1]  
        risk_value = self.state[2]  
        renewable_absorption = self.state[3]  

        reward = -(thermal_cost + carbon_cost + risk_value - renewable_absorption)

        
        done = self.step_counter >= 100


        return self.state, reward, done, {}


    def reset(self):
        # 重置环境到初始状态
        self.state = np.random.rand(4) * 10  # 修改为4维
        # 重置步数计数器
        self.step_counter = 0
        return self.state