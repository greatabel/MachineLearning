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
    dense1 = Dense(400, activation="relu")(state_input)
    dense2 = Dense(300, activation="relu")(dense1)
    action_output = Dense(action_dim, activation="tanh")(dense2)

    model = Model(state_input, action_output)
    return model


# 定义评论家网络
def create_critic_model(state_dim, action_dim):
    state_input = Input((state_dim,))
    action_input = Input((action_dim,))
    input = Concatenate()([state_input, action_input])
    dense1 = Dense(400, activation="relu")(input)
    dense2 = Dense(300, activation="relu")(dense1)
    q_output = Dense(1, activation=None)(dense2)

    model = Model([state_input, action_input], q_output)
    return model


class EdgeComputingEnv(gym.Env):
    def __init__(self, bandwidth=1.0, noise_power=1.0, num_tasks=5):
        super(EdgeComputingEnv, self).__init__()
        self.bandwidth = bandwidth  # 信道的带宽
        self.noise_power = noise_power  # 噪声的功率
        self.num_tasks = num_tasks  # 同时处理的任务数量
        self.task_queue = []  # 任务队列
        self.state_dim = self.num_tasks * 4  # 状态维度：每个任务的计算量、传输量、距离、任务大小
        self.action_dim = self.num_tasks * 2  # 动作维度：每个任务的缓存量和卸载量
        self.task_count = 0  # 已处理任务的数量

        # 动作空间和状态空间
        self.action_space = spaces.Box(
            low=0, high=1, shape=(self.action_dim,), dtype=np.float32
        )
        self.observation_space = spaces.Box(
            low=0, high=np.inf, shape=(self.state_dim,), dtype=np.float32
        )

    def step(self, action):
        total_time = 0
        total_energy = 0  # 新增一个变量来存储总能耗
        fi = 1.0  # 假设每个设备的计算能力为1.0，可以随机修改
        pi = 0.1  # 假设每个设备的功耗为0.1，可以随机修改

        for i in range(self.num_tasks):
            # 根据动作更新环境状态
            cache, offload = action[i*2:i*2+2]
            compute, transmit, distance, task_size = self.task_queue.pop(0)

            # 根据香农公式计算传输速率
            signal_power = 1.0 / (distance ** 2)  # 假设信号功率与距离的平方成反比
            transmission_rate = self.bandwidth * np.log2(1 + signal_power / self.noise_power)

            # 考虑本地处理的部分
            local = compute - cache - offload
            if local > 0:  # 如果有部分任务在本地处理
                # 本地处理的时间等于任务大小除以设备的计算能力
                local_time = local / fi  
                # 本地处理的能耗等于功耗乘以处理时间
                local_energy = pi * local_time  
            else:  # 如果任务被完全卸载
                local_time = 0
                local_energy = 0

            offload_time = offload + cache  # 卸载处理的时间
            transmit_time = task_size / transmission_rate  # 计算传输时间
            time = offload_time + local_time + transmit_time  # 总的完成时间等于卸载处理时间、本地处理时间和传输时间之和
            energy = local_energy  # 总能耗等于本地处理的能耗

            total_time += time
            total_energy += energy
            self.task_count += 1  # 已处理任务的数量增加

            # 如果任务队列为空，那么我们添加新的任务
            while len(self.task_queue) < self.num_tasks:
                self.task_queue.append(self._new_task())

        # 下一个状态就是任务队列中的所有任务
        next_state = np.array([task for task in self.task_queue], dtype=np.float32).flatten()

        # 奖励函数是负的完成时间和能耗
        reward = -total_time - total_energy

        # 如果已处理任务的数量超过100，那么环境结束
        done = self.task_count >= 100 * self.num_tasks

        return next_state, reward, done, {}


    def reset(self):
        # 重置环境
        self.task_queue = [self._new_task() for _ in range(self.num_tasks)]
        return np.array([task for task in self.task_queue], dtype=np.float32).flatten()

    def _new_task(self):
        # 创建一个新的任务，计算量、传输量、距离和任务大小都是在特定范围内随机生成的
        return [
            np.random.uniform(1, 10),
            np.random.uniform(1, 10),
            np.random.uniform(10, 100),
            np.random.uniform(1, 5),
        ]


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
