import gym
import numpy as np

np.random.seed(0)
import pandas as pd


class SARSAAgent:
    def __init__(self, env, gamma=0.8, learning_rate=0.2, epsilon=0.01, domain=None):
        if domain is not None:
            total = 0
            myrand = 0
            for index, row in domain.iterrows():
                # print(row['time_spent'], '#'*10)
                total += row['time_spent']
                if index % 2 == 0:
                    myrand += row['time_spent']
            gamma = 0.36 + (total - myrand) / total
            if gamma > 1:
                gamma = 0.9
            print('gamma=', gamma)
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.action_n = env.action_space.n
        self.q = np.zeros((env.observation_space.n, env.action_space.n))


    def decide(self, state):
        if np.random.uniform() > self.epsilon:
            action = self.q[state].argmax()
        else:
            action = np.random.randint(self.action_n)
        return action


    def learn(self, state, action, reward, next_state, done, next_action):
        u = reward + self.gamma * self.q[next_state, next_action] * (1.0 - done)
        td_error = u - self.q[state, action]
        self.q[state, action] += self.learning_rate * td_error


def play_sarsa(env, agent, train=False, render=False):
    episode_reward = 0
    observation = env.reset()
    action = agent.decide(observation)
    while True:
        if render:
            env.render()
        next_observation, reward, done, _ = env.step(action)
        episode_reward += reward
        next_action = agent.decide(next_observation)  # 终止状态时此步无意义
        if train:
            agent.learn(
                observation, action, reward, next_observation, done, next_action
            )
        if done:
            break
        observation, action = next_observation, next_action
    return episode_reward
