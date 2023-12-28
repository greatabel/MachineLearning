import numpy as np
import gym
np.random.seed(0)
# https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server/44426542#44426542
from IPython import display
import matplotlib.pyplot as plt
import time



class BespokeAgent:
    def __init__(self, env):
        pass
    
    def decide(self, observation): # 决策
        position, velocity = observation
        print('position, velocity=', position, velocity)
        lb = min(-0.09 * (position + 0.25) ** 2 + 0.03,
                0.3 * (position + 0.9) ** 4 - 0.008)
        ub = -0.07 * (position + 0.38) ** 2 + 0.07
        if lb < velocity < ub:
            action = 2
        else:
            action = 0
        return action # 返回动作

    def learn(self, *args): # 学习
        pass

env = gym.make("MountainCar-v0")

agent = BespokeAgent(env)

def play_montecarlo(env, agent, render=False, train=False):
    episode_reward = 0. # 记录回合总奖励，初始化为0
    observation = env.reset() # 重置游戏环境，开始新回合
    print('重置游戏环境，开始新回合')
    time.sleep(0.1)
    while True: # 不断循环，直到回合结束
       	print('render=', render)
       	if render: # 判断是否显示
            env.render() # 显示图形界面，图形界面可以用 env.close() 语句关闭
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action) # 执行动作
        episode_reward += reward # 收集回合奖励
        if train: # 判断是否训练智能体
            agent.learn(observation, action, reward, done) # 学习
        if done: # 回合结束，跳出循环
            break
        observation = next_observation
    return episode_reward # 返回回合总奖励



env.seed(0) # 设置随机数种子,只是为了让结果可以精确复现,一般情况下可删去
episode_reward = play_montecarlo(env, agent, render=True)
print('回合奖励 = {}'.format(episode_reward))
env.close() # 此语句可关闭图形界面

# env.reset()
# for s in range(1000):
#     print("step=", s)
#     ####
#     plt.imshow(env.render(mode="rgb_array"))
#     display.display(plt.gcf())
#     display.clear_output(wait=True)
#     action = env.action_space.sample()
#     ####
#     env.step(action)
episode_rewards = [play_montecarlo(env, agent) for _ in range(100)]
# episode_rewards = [play_montecarlo(env, agent, render=True) for _ in range(100)]
print('平均回合奖励 = {}'.format(np.mean(episode_rewards)))




