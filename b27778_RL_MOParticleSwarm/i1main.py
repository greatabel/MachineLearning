import gym
from gym import spaces
import numpy as np
import matplotlib.pyplot as plt
from i0common import *




# 客观观察函数
def objective_function(particle):
    cost = np.abs(np.sin(particle[0])) + 0.1 * np.abs(particle[0])
    risk = np.abs(np.cos(particle[1])) + 0.1 * np.abs(particle[1])
    renewable_consumption = np.abs(20 - np.abs(np.sin(particle[2])) * np.abs(particle[2]))
    
    # 假设希望最大化光伏出力，并且对大幅度的出力变化进行惩罚
    pv_output = particle[3]

    
    return np.array([cost, risk, renewable_consumption, pv_output])



# 奖励函数
def reward_function(new_solution, current_solution):
    improvement = objective_function(current_solution) - objective_function(new_solution)
    return np.sum(np.maximum(improvement, 0))



# Q-learning参数
alpha = 0.1
gamma = 0.9
epsilon = 0.1
num_episodes = 100

w = 0.7
c1 = 2
c2 = 2



# RL-MOPSO参数
num_particles_rl_mopso = 25
num_iterations_rl_mopso = 200  # 增加迭代次数

# 传统MOPSO参数
num_particles_traditional_mopso = 25
num_iterations_traditional_mopso = 300  # 增加迭代次数

# 创建环境
env = PowerPlantEnv()

# 初始化Q-table
# 初始化Q-table
q_table = np.random.uniform(low=-1, high=1, size=(20, 20, 20, 20, env.action_space.n))  # 修改为4个维度


# 初始化RL-MOPSO
particles_rl_mopso = np.random.rand(num_particles_rl_mopso, 4) * 10
pbest_rl_mopso = np.copy(particles_rl_mopso)
gbest_rl_mopso = np.min(pbest_rl_mopso, axis=0)
velocities_rl_mopso = np.zeros_like(particles_rl_mopso)

# 初始化传统MOPSO
particles_traditional_mopso = np.random.rand(num_particles_traditional_mopso, 4) * 10
pbest_traditional_mopso = np.copy(particles_traditional_mopso)
gbest_traditional_mopso = np.min(pbest_traditional_mopso, axis=0)
velocities_traditional_mopso = np.zeros_like(particles_traditional_mopso)

# 存储性能数据
rl_mopso_cost = []
rl_mopso_risk = []
rl_mopso_renewable_consumption = []
traditional_mopso_cost = []
traditional_mopso_risk = []
traditional_mopso_renewable_consumption = []

# 训练Q-learning模型
rewards = []
for i in range(num_episodes):
    state = env.reset()
    done = False
    episode_reward = 0

    while not done:
        # 将状态离散化以适应Q-table
        discrete_state = (state - env.observation_space.low) / (env.observation_space.high - env.observation_space.low)
        discrete_state = tuple((discrete_state * 20).astype(int))

        # 限制discrete_state的值在有效范围内
        discrete_state = tuple(np.clip(discrete_state, 0, 19))

        # 使用epsilon-greedy策略选择动作
        if np.random.random() < epsilon:
            action = np.random.choice(env.action_space.n)  # 随机选择一个动作
        else:
            action = int(np.argmax(q_table[discrete_state]))  # 选择具有最大Q值的动作

        # 执行动作
        next_state, reward, done, _ = env.step(action)
        episode_reward += reward

        # 将下一个状态离散化
        discrete_next_state = (next_state - env.observation_space.low) / (env.observation_space.high - env.observation_space.low)
        discrete_next_state = tuple((discrete_next_state * 20).astype(int))

        # 限制discrete_next_state的值在有效范围内
        discrete_next_state = tuple(np.clip(discrete_next_state, 0, 19))

        # 更新Q-table
        max_future_q = np.max(q_table[discrete_next_state])
        current_q = q_table[discrete_state + (action,)]
        new_q = (1 - alpha) * current_q + alpha * (reward + gamma * max_future_q)
        q_table[discrete_state + (action,)] = new_q

        state = next_state

    rewards.append(episode_reward)

    # 计算RL-MOPSO的成本、风险和可再生能源消耗比例
    rl_mopso_cost.append(np.abs(np.sin(gbest_rl_mopso[0])) + 0.1 * np.abs(gbest_rl_mopso[0]))
    rl_mopso_risk.append(np.abs(np.cos(gbest_rl_mopso[1])) + 0.1 * np.abs(gbest_rl_mopso[1]))
    rl_mopso_renewable_consumption.append(np.abs(20 - np.abs(np.sin(gbest_rl_mopso[2])) * np.abs(gbest_rl_mopso[2])))

    print(f"Episode {i+1} completed with total reward {episode_reward}")

# RL-MOPSO主循环
for iteration in range(num_iterations_rl_mopso):
    for i in range(num_particles_rl_mopso):
        # 更新速度
        r1, r2 = np.random.rand(), np.random.rand()
        velocities_rl_mopso[i] = w * velocities_rl_mopso[i] + c1 * r1 * (pbest_rl_mopso[i] -
                                 particles_rl_mopso[i]) + c2 * r2 * (gbest_rl_mopso - particles_rl_mopso[i])

        # 更新位置
        particles_rl_mopso[i] += velocities_rl_mopso[i]

        # 更新个体最优解
        if reward_function(particles_rl_mopso[i], pbest_rl_mopso[i]) > 0:
            pbest_rl_mopso[i] = particles_rl_mopso[i]

    # 强化学习部分 - Q-learning
    rewards = np.zeros(env.action_space.n)
    for i in range(num_particles_rl_mopso):
        for action in range(env.action_space.n):
            new_solution = particles_rl_mopso[i] + (pbest_rl_mopso[i] - particles_rl_mopso[i]) * np.random.uniform(-1, 1, 4)

            rewards[action] += reward_function(new_solution, particles_rl_mopso[i])

        # Q-learning更新
        current_state = tuple(np.clip((particles_rl_mopso[i] - env.observation_space.low) / 
                        (env.observation_space.high - env.observation_space.low) * 20, 0, 19).astype(int))
        best_action = np.argmax(rewards)
        q_table[current_state + (best_action,)] = (1 - alpha) * q_table[current_state + (best_action,)] + alpha * (rewards[best_action])

        # 选择最佳动作
        best_action = np.argmax(q_table[current_state, :])

        # 执行动作
        particles_rl_mopso[i] += (pbest_rl_mopso[i] - particles_rl_mopso[i]) * np.random.uniform(-1, 1, 4)

    # 更新全局最优解
    current_pbest_rl_mopso = np.min(pbest_rl_mopso, axis=0)
    if reward_function(current_pbest_rl_mopso, gbest_rl_mopso) > 0:
        gbest_rl_mopso = current_pbest_rl_mopso

    # 记录RL-MOPSO的成本、风险和可再生能源消耗比例
    rl_mopso_cost.append(np.abs(np.sin(gbest_rl_mopso[0])) + 0.1 * np.abs(gbest_rl_mopso[0]))
    rl_mopso_risk.append(np.abs(np.cos(gbest_rl_mopso[1])) + 0.1 * np.abs(gbest_rl_mopso[1]))
    rl_mopso_renewable_consumption.append(np.abs(20 - np.abs(np.sin(gbest_rl_mopso[2])) * np.abs(gbest_rl_mopso[2])))

# 传统MOPSO主循环
for iteration in range(num_iterations_traditional_mopso):
    for i in range(num_particles_traditional_mopso):
        # 更新速度
        r1, r2 = np.random.rand(), np.random.rand()
        velocities_traditional_mopso[i] = w * velocities_traditional_mopso[i] + c1 * r1 * (pbest_traditional_mopso[i] -
                                        particles_traditional_mopso[i]) + c2 * r2 * (gbest_traditional_mopso - particles_traditional_mopso[i])

        # 更新位置
        particles_traditional_mopso[i] += velocities_traditional_mopso[i]

        # 更新个体最优解
        if reward_function(particles_traditional_mopso[i], pbest_traditional_mopso[i]) > 0:
            pbest_traditional_mopso[i] = particles_traditional_mopso[i]

    # 更新全局最优解
    current_pbest_traditional_mopso = np.min(pbest_traditional_mopso, axis=0)
    if reward_function(current_pbest_traditional_mopso, gbest_traditional_mopso) > 0:
        gbest_traditional_mopso = current_pbest_traditional_mopso

    # 记录传统MOPSO的成本、风险和可再生能源消耗比例
    traditional_mopso_cost.append(np.abs(np.sin(gbest_traditional_mopso[0])) + 0.1 * np.abs(gbest_traditional_mopso[0]))
    traditional_mopso_risk.append(np.abs(np.cos(gbest_traditional_mopso[1])) + 0.1 * np.abs(gbest_traditional_mopso[1]))
    traditional_mopso_renewable_consumption.append(np.abs(20 - np.abs(np.sin(gbest_traditional_mopso[2])) * np.abs(gbest_traditional_mopso[2])))


# 绘制对比图
plt.figure(figsize=(10, 5))
plt.plot(rl_mopso_cost, label='RL-MOPSO Cost', linestyle='dashed')
plt.plot(traditional_mopso_cost, label='Traditional MOPSO Cost')
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.legend()
plt.title('RL-MOPSO vs Traditional MOPSO - Cost')
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(rl_mopso_risk, label='RL-MOPSO Risk', linestyle='dashed')
plt.plot(traditional_mopso_risk, label='Traditional MOPSO Risk')
plt.xlabel('Iterations')
plt.ylabel('Risk')
plt.legend()
plt.title('RL-MOPSO vs Traditional MOPSO - Risk')
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(rl_mopso_renewable_consumption, label='RL-MOPSO Renewable Consumption', linestyle='dashed')
plt.plot(traditional_mopso_renewable_consumption, label='Traditional MOPSO Renewable Consumption')
plt.xlabel('Iterations')
plt.ylabel('Renewable Consumption')
plt.legend()
plt.title('RL-MOPSO vs Traditional MOPSO - Renewable Consumption')
plt.show()
