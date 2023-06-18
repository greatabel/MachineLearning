import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from gym import spaces
import gym
import matplotlib.pyplot as plt


# 定义演员网络
def create_actor_model(state_dim, action_dim):
    state_input = Input((state_dim,))
    dense1 = Dense(400, activation='relu')(state_input)
    dense2 = Dense(300, activation='relu')(dense1)
    action_output = Dense(action_dim, activation='tanh')(dense2)

    model = Model(state_input, action_output)
    return model

# 定义评论家网络
def create_critic_model(state_dim, action_dim):
    state_input = Input((state_dim,))
    action_input = Input((action_dim,))
    input = Concatenate()([state_input, action_input])
    dense1 = Dense(400, activation='relu')(input)
    dense2 = Dense(300, activation='relu')(dense1)
    q_output = Dense(1, activation=None)(dense2)

    model = Model([state_input, action_input], q_output)
    return model

class EdgeComputingEnv(gym.Env):
    def __init__(self):
        super(EdgeComputingEnv, self).__init__()
        self.task_queue = []  # 任务队列
        self.state_dim = 2  # 状态维度：当前任务的计算量和传输量
        self.action_dim = 2  # 动作维度：缓存量和卸载量
        self.task_count = 0  # 已处理任务的数量

        # 动作空间和状态空间
        self.action_space = spaces.Box(low=0, high=1, shape=(self.action_dim,), dtype=np.float32)
        self.observation_space = spaces.Box(low=0, high=np.inf, shape=(self.state_dim,), dtype=np.float32)

    def step(self, action):
        # 根据动作更新环境状态
        cache, offload = action
        compute, transmit = self.task_queue.pop(0)
        compute -= cache + offload
        transmit -= offload
        time = compute + transmit  # 假计算和传输的时间都是线性的
        self.task_count += 1  # 已处理任务的数量增加

        # 如果任务队列为空，那么我们添加一个新的任务
        if not self.task_queue:
            self.task_queue.append(self._new_task())

        # 下一个状态就是任务队列中的下一个任务
        next_state = np.array(self.task_queue[0], dtype=np.float32)

        # 奖励函数是负的完成时间
        reward = -time

        # 如果已处理任务的数量超过100，那么环境结束
        done = self.task_count >= 100

        return next_state, reward, done, {}

    def reset(self):
        # 重置环境
        self.task_queue = [self._new_task()]
        return np.array(self.task_queue[0], dtype=np.float32)

    def _new_task(self):
        # 创建一个新的任务，计算量和传输量都是随机的
        return [np.random.rand() * 10, np.random.rand() * 10]

class ReplayBuffer:
    def __init__(self, capacity=10000):
        self.buffer = []
        self.capacity = capacity

    def record(self, experience):
        if len(self.buffer) >= self.capacity:
            self.buffer.pop(0)
        self.buffer.append(experience)

    def sample(self, batch_size):
        indices = np.random.choice(len(self.buffer), batch_size)
        return [self.buffer[i] for i in indices]

def evaluate_model(env, actor_model, num_episodes=100):
    total_reward = 0
    total_steps = 0
    total_tasks = 0

    for i in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            if actor_model is None:
                # 如果没有模型，就选择随机动作
                action = env.action_space.sample()
            else:
                # 如果有模型，就使用模型预测动作
                action = actor_model.predict(np.array([state]))[0]

            next_state, reward, done, _ = env.step(action)

            total_reward += reward
            total_steps += 1
            total_tasks += len(env.task_queue)

            state = next_state

    avg_reward = total_reward / num_episodes
    avg_steps = total_steps / num_episodes
    avg_tasks = total_tasks / num_episodes

    return avg_reward, avg_steps, avg_tasks

