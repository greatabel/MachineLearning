import numpy as np
import gym

from colored import fg, bg, attr
# 使用 fg (前景色), bg (背景色) 和 attr (属性, 如重置)
red_text = fg('red')
green_background = bg('green')
reset = attr('reset')


np.random.seed(0)
env = gym.make('FrozenLake-v1', render_mode='ansi')

print('观察空间 = {}'.format(env.observation_space))
print('动作空间 = {}'.format(env.action_space))
print('观测空间大小 = {}'.format(env.observation_space.n))
print('动作空间大小 = {}'.format(env.action_space.n))

# 查看特定状态和动作下的转移概率
env.unwrapped.P[14][2]

def play_policy(env, policy, render=False):
    total_reward = 0.
    observation = env.reset()
    state = observation[0] if isinstance(observation, tuple) else observation  # 状态解析
    while True:
        if render:
            rendered = env.render()
            # print(rendered)
        action = np.random.choice(env.action_space.n, p=policy[state])
        r = env.step(action)
        print('r=', r)
        observation, reward, done, _, _ = r
        if reward != 0.0:
        	print(green_background + 'r==> ' + str(r) + reset)
        state = observation[0] if isinstance(observation, tuple) else observation  # 更新状态
        total_reward += reward
        if done:
            break
    return total_reward




# 随机策略
random_policy = np.ones((env.observation_space.n, env.action_space.n)) / env.action_space.n

episode_rewards = [play_policy(env, random_policy, True) for _ in range(100)]
print("随机策略 平均奖励：{}".format(np.mean(episode_rewards)))
