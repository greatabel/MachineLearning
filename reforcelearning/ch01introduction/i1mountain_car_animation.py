import gym

# https://stackoverflow.com/questions/40195740/how-to-run-openai-gym-render-over-a-server/44426542#44426542
from IPython import display
import matplotlib.pyplot as plt
import time


env = gym.make("MountainCar-v0")


# print('观测空间 = {}'.format(env.observation_space))
# print('动作空间 = {}'.format(env.action_space))
# print('观测范围 = {} ~ {}'.format(env.observation_space.low,
#         env.observation_space.high))
# print('动作数 = {}'.format(env.action_space.n))

env.reset()
for s in range(1000):
    print("step=", s)
    ####
    plt.imshow(env.render(mode="rgb_array"))
    display.display(plt.gcf())
    display.clear_output(wait=True)
    action = env.action_space.sample()
    ####
    env.step(action)

env.close()
