import gym

# https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server/44426542#44426542
from IPython import display
import matplotlib.pyplot as plt
import time


env = gym.make("Taxi-v3")
env.seed(0)
print('观测空间 = {}'.format(env.observation_space))
print('动作空间 = {}'.format(env.action_space))
print('状态数量 = {}, 动作数量 = {}'.format(env.nS, env.nA))

env.reset()
for s in range(10):
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
