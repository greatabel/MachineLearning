import numpy as np
np.random.seed(0)

import pandas as pd
import gym

#https://stackoverflow.com/questions/33589196/ipython-importerror-no-module-named-display
from IPython.display import display
#查看Gym注册了哪些环境

env_specs = gym.envs.registry.all()
env_ids = [env_spec.id for env_spec in env_specs]
print(env_ids)
print(len(env_ids))


space_names = ['观测空间', '动作空间', '奖励范围', '最大步数']
df = pd.DataFrame(columns=space_names)

env_specs = gym.envs.registry.all()
for env_spec in env_specs:
    env_id = env_spec.id
    try:
        env = gym.make(env_id)
        observation_space = env.observation_space
        action_space = env.action_space
        reward_range = env.reward_range
        max_episode_steps = None
        if isinstance(env, gym.wrappers.time_limit.TimeLimit):
            max_episode_steps = env._max_episode_steps
        df.loc[env_id] = [observation_space, action_space, reward_range, max_episode_steps]
    except:
        pass

with pd.option_context('display.max_rows', None):
    display(df)