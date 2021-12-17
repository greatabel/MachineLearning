import numpy as np
np.random.seed(0)

import pandas as pd
import gym

#查看Gym注册了哪些环境

env_specs = gym.envs.registry.all()
env_ids = [env_spec.id for env_spec in env_specs]
print(env_ids)
print(len(env_ids))