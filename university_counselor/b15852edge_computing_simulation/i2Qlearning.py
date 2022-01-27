import gym
import numpy as np

np.random.seed(0)
import pandas as pd


class ExpectedSARSAAgent:
    def __init__(self, env, gamma=0.9, learning_rate=0.1, epsilon=0.01, domain=None):
        if domain is not None:
            total = 0
            myrand = 0
            for index, row in domain.iterrows():
                # print(row['time_spent'], '#'*10)
                total += row['time_spent']
                if index % 2 == 0:
                    myrand += row['time_spent']
            gamma = 0.41 + (total - myrand) / total
            if gamma > 1 or gamma < 0.9:
                gamma = 0.9
            print('gamma=', gamma)
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.epsilon = epsilon
        self.q = np.zeros((env.observation_space.n, env.action_space.n))
        self.action_n = env.action_space.n

    def decide(self, state):
        if np.random.uniform() > self.epsilon:
            action = self.q[state].argmax()
        else:
            action = np.random.randint(self.action_n)
        return action

    def learn(self, state, action, reward, next_state, done):
        v = self.q[next_state].mean() * self.epsilon + self.q[next_state].max() * (
            1.0 - self.epsilon
        )
        u = reward + self.gamma * v * (1.0 - done)
        td_error = u - self.q[state, action]
        self.q[state, action] += self.learning_rate * td_error


def play_qlearning(env, agent, train=False, render=False):
    episode_reward = 0
    observation = env.reset()
    while True:
        if render:
            env.render()
        action = agent.decide(observation)
        next_observation, reward, done, _ = env.step(action)
        episode_reward += reward
        if train:
            agent.learn(observation, action, reward, next_observation, done)
        if done:
            break
        observation = next_observation
    return episode_reward
