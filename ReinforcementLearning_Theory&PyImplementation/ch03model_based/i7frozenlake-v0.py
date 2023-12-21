#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import gym


np.random.seed(0)
env = gym.make('FrozenLake-v1', render_mode='ansi')

print('观察空间 = {}'.format(env.observation_space))
print('动作空间 = {}'.format(env.action_space))
print('观测空间大小 = {}'.format(env.observation_space.n))
print('动作空间大小 = {}'.format(env.action_space.n))

# 查看特定状态和动作下的转移概率
print(
    'env.unwrapped.P[14][2]=',
    env.unwrapped.P[14][2]
)

print('''
转移概率：执行这个动作后转移到新状态的概率。
新状态：如果执行这个动作，可能到达的新状态。
奖励：执行这个动作后获得的即时奖励。
是否终止：这个新状态是否是终止状态（游戏结束）
''')






# In[14]:


from IPython.display import clear_output
import time

def play_policy(env, policy, render=False):
    total_reward = 0.
    observation = env.reset()
    state = observation[0] if isinstance(observation, tuple) else observation  # 状态解析
    while True:
        if render:
            rendered = env.render()  # 使用 ansi 模式渲染并获取返回值
            clear_output(wait=True)
            print(rendered)  # 打印渲染的输出
            time.sleep(0.001)  # 暂停一段时间以便观察
        action = np.random.choice(env.action_space.n, p=policy[state])
        r = env.step(action)
        # print('r=', r)
        observation, reward, done, _, _ = r
        state = observation[0] if isinstance(observation, tuple) else observation  # 更新状态
        total_reward += reward
        if done:
            break
    return total_reward


# In[17]:


# 随机策略
random_policy = np.ones((env.observation_space.n, env.action_space.n)) / env.action_space.n
# print('random_policy=',random_policy)

episode_rewards = [play_policy(env, random_policy, True) for _ in range(100)]
print("随机策略 平均奖励：{}".format(np.mean(episode_rewards)))


# # 其中 S 表示起点，F 表示冰面，H 表示坑洞，G 表示目标
# ## 尝试达到目标位置 G 而避免掉入坑洞 H

# ### 策略评估

# In[4]:


def v2q(env, v, s=None, gamma=1.): # 根据状态价值函数计算动作价值函数
    if s is not None: # 针对单个状态求解
        q = np.zeros(env.action_space.n)
        for a in range(env.action_space.n):
            for prob, next_state, reward, done in env.unwrapped.P[s][a]:
                q[a] += prob * \
                        (reward + gamma * v[next_state] * (1. - done))
    else: # 针对所有状态求解
        q = np.zeros((env.observation_space.n, env.action_space.n))
        for s in range(env.observation_space.n):
            q[s] = v2q(env, v, s, gamma)
    return q

def evaluate_policy(env, policy, gamma=1., tolerant=1e-6):
    v = np.zeros(env.observation_space.n) # 初始化状态价值函数
    while True: # 循环
        delta = 0
        for s in range(env.observation_space.n):
            vs = sum(policy[s] * v2q(env, v, s, gamma)) # 更新状态价值函数
            delta = max(delta, abs(v[s]-vs)) # 更新最大误差
            v[s] = vs # 更新状态价值函数
        if delta < tolerant: # 查看是否满足迭代条件
            break
    return v


# In[5]:


print('状态价值函数：')
v_random = evaluate_policy(env, random_policy)
print(v_random.reshape(4, 4))

print('动作价值函数：')
q_random = v2q(env, v_random)
print(q_random)


# ### 策略改进

# In[6]:


def improve_policy(env, v, policy, gamma=1.):
    optimal = True
    for s in range(env.observation_space.n):
        q = v2q(env, v, s, gamma)
        a = np.argmax(q)
        if policy[s][a] != 1.:
            optimal = False
            policy[s] = 0.
            policy[s][a] = 1.
    return optimal


# In[7]:


policy = random_policy.copy()
optimal = improve_policy(env, v_random, policy)
if optimal:
    print('无更新，最优策略为：')
else:
    print('有更新，更新后的策略为：')
print(policy)


# In[8]:


# 策略迭代
def iterate_policy(env, gamma=1., tolerant=1e-6):
     # 初始化为任意一个策略
    policy = np.ones((env.observation_space.n, env.action_space.n)) \
            / env.action_space.n
    while True:
        v = evaluate_policy(env, policy, gamma, tolerant) # 策略评估
        if improve_policy(env, v, policy): # 策略改进
            break
    return policy, v

policy_pi, v_pi = iterate_policy(env)
print('状态价值函数 =')
print(v_pi.reshape(4, 4))
print('最优策略 =')
print(np.argmax(policy_pi, axis=1).reshape(4, 4))


# In[9]:


#测试策略
episode_rewards = [play_policy(env, policy_pi)  for _ in range(100)]
print("策略迭代 平均奖励：{}".format(np.mean(episode_rewards)))


# ### 价值迭代
# 

# In[10]:


def iterate_value(env, gamma=1, tolerant=1e-6):
    v = np.zeros(env.observation_space.n) # 初始化
    while True:
        delta = 0
        for s in range(env.observation_space.n):
            vmax = max(v2q(env, v, s, gamma)) # 更新价值函数
            delta = max(delta, abs(v[s]-vmax))
            v[s] = vmax
        if delta < tolerant: # 满足迭代需求
            break
            
    policy = np.zeros((env.observation_space.n, env.action_space.n)) # 计算最优策略
    for s in range(env.observation_space.n):
        a = np.argmax(v2q(env, v, s, gamma))
        policy[s][a] = 1.
    return policy, v

policy_vi, v_vi = iterate_value(env)
print('状态价值函数 =')
print(v_vi.reshape(4, 4))
print('最优策略 =')
print(np.argmax(policy_vi, axis=1).reshape(4, 4))


# In[11]:


# 测试策略
episode_rewards = [play_policy(env, policy_vi, True) for _ in range(100)]
print("价值迭代 平均奖励：{}".format(np.mean(episode_rewards)))


# In[ ]:





# In[ ]:





# In[ ]:




