import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Input, Dense, Concatenate
from tensorflow.keras.models import Model
from gym import spaces
import gym
import matplotlib.pyplot as plt
from i2common import *


def main():
    env = EdgeComputingEnv()
    results = []

    # 不使用DDPG模型评估环境
    avg_reward, avg_steps, avg_tasks = evaluate_model(env, None)
    results.append(('Without DDPG', avg_reward, avg_steps, avg_tasks))
    print("Without DDPG:")
    print(f"Average Reward: {avg_reward}, Average Steps: {avg_steps}, Average Task Queue Length: {avg_tasks}")

    # 使用DDPG模型评估环境
    actor_model = create_actor_model(env.state_dim, env.action_dim)  # 创建演员模型
    actor_model.load_weights("actor_model_weights.h5")  # 加载训练好的演员模型权重文件
    avg_reward, avg_steps, avg_tasks = evaluate_model(env, actor_model)
    results.append(('With DDPG', avg_reward, avg_steps, avg_tasks))
    print("With DDPG:")
    print(f"Average Reward: {avg_reward}, Average Steps: {avg_steps}, Average Task Queue Length: {avg_tasks}")

    # 绘制对比图
    labels, rewards, steps, tasks = zip(*results)

    x = range(len(labels))

    plt.figure(figsize=(15,5))

    plt.subplot(1,3,1)
    plt.bar(x, rewards, tick_label=labels)
    plt.title('Average Reward')

    plt.subplot(1,3,2)
    plt.bar(x, steps, tick_label=labels)
    plt.title('Average Steps')

    plt.subplot(1,3,3)
    plt.bar(x, tasks, tick_label=labels)
    plt.title('Average Task Queue Length')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()