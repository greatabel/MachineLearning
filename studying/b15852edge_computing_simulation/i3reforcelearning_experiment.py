import gym
import numpy as np

np.random.seed(0)
import pandas as pd
from termcolor import colored

# https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server/44426542#44426542
from IPython import display
import matplotlib.pyplot as plt
import time
import datetime


from i1heuristic_algorithm import SARSAAgent, play_sarsa
from i2Qlearning import ExpectedSARSAAgent, play_qlearning

"""
不同GPU功耗（以占有率作为指标）/时延（以API的起始时间为指标）为不同条件
比较不同调度算法下进行对比，进行可视化
"""
def show(s,color='green'):
    print(colored(s, color, attrs=['reverse', 'blink']), now_time())

def now_time():
    return datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")


def Load_mapping_experiment(custom_domain, category='heat_heavy'):

    print("-" * 20, "step 0")
    env = gym.make("Taxi-v3")
    env.seed(0)
    print("建立负载映射环境对应关系")
    print("观测空间 = {}".format(env.observation_space))
    print("动作空间 = {}".format(env.action_space))
    print("状态数量 = {}, 动作数量 = {}".format(env.nS, env.nA))

    env.reset()
    for s in range(3):
        print("step=", s)
        ####
        # plt.imshow(env.render(mode="rgb_array"))
        # display.display(plt.gcf())
        # display.clear_output(wait=True)
        env.render()
        action = env.action_space.sample()
        ####
        env.step(action)

    env.close()

    print("-" * 20, "step 1")
    state = env.reset()
    taxirow, taxicol, passloc, destidx = env.unwrapped.decode(state)
    print(taxirow, taxicol, passloc, destidx)
    print("模拟运载程序块位置 = {}".format((taxirow, taxicol)))
    print("模拟访问和计算程序内存位置 = {}".format(env.unwrapped.locs[passloc]))
    print("目标位置 = {}".format(env.unwrapped.locs[destidx]))
    env.render()

    print("-" * 20, "step 2")
    env.step(0)
    env.render()

    print("--------------------", "step 3")
    heat = custom_domain.loc[custom_domain['function'] == category]
    show("%s" %heat)
    heat_data = []

    print("启发式算法模拟")
    agent = SARSAAgent(env, domain=heat)

    # 训练
    episodes = 5000
    episode_rewards = []
    for episode in range(episodes):
        episode_reward = play_sarsa(env, agent, train=True)
        episode_rewards.append(episode_reward)

    plt.plot(episode_rewards)
    plt.savefig("i1heuristic_algorithm_"+category+".png")
    # 清理绘图为下一个算法做准备
    plt.clf()
    # 测试
    agent.epsilon = 0.0  # 取消探索

    episode_rewards = [play_sarsa(env, agent) for _ in range(100)]
    av = np.mean(episode_rewards)
    print(
        "平均回合奖励 = {} / {} = {}".format(
            sum(episode_rewards), len(episode_rewards), av
        )
    )
    heat_data.append(av)


    print("--------------------", "step 4")
    print("QLearning算法模拟")
    agent = ExpectedSARSAAgent(env, domain=heat)

    # 训练
    episodes = 5000
    episode_rewards = []
    for episode in range(episodes):
        episode_reward = play_qlearning(env, agent, train=True)
        episode_rewards.append(episode_reward)

    plt.plot(episode_rewards)
    plt.savefig("i2qlearning_"+category+".png")
    plt.clf()
    # 测试
    agent.epsilon = 0.0  # 取消探索

    episode_rewards = [play_qlearning(env, agent) for _ in range(100)]
    av = np.mean(episode_rewards)
    print(
        "平均回合奖励 = {} / {} = {}".format(
            sum(episode_rewards), len(episode_rewards), av
        )
    )
    heat_data.append(av)

    labels = ['heuristic', 'qlearning']
    plt.bar(range(len(heat_data)), heat_data, tick_label=labels, color=['r', 'g', 'b'])
    # plt.show()

    plt.savefig(category+"_compare.png")


if __name__ == "__main__":
    Load_mapping_experiment()