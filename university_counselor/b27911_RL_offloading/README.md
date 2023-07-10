# 部署文档

1.
安装python3.6 以上版本

2. 
安装pip3 

3.
可选  可以不做（创建python3虚拟目录，隔绝不同版本库之间相互影响）
https://docs.python.org/zh-cn/3/tutorial/venv.html

4.
4.1
terminal底下进入工程目录下，在requirements.txt同级目录下运行：
pip install --upgrade -r requirements.txt



6.
数据探索 可视化
python3 i1ddpg_evaluate.py


7.（可选，可以不用部署运行，已经运行出结果，并缓存）
python3 i0ddpg_train.py







# ---- start of requirements ------

训练部分
创建DDPG深度强化学习模型：创建actor模型（策略网络）和critic_model模型（价值网络），
这两个网络将会在训练过程中共同学习如何在环境中执行最优动作。

2.
实现记忆回放：创建了一个记忆回放缓冲区，用于存储和采样过去的经验，以训练模型。

3.
模型训练：对演员和评论家模型进行训练，以在环境中学习最优策略。
模型更新：使用目标网络和经验回放，来稳定的更新演员和评论家模型。

4.
(可选)
加载训练模型：加载训练好的演员模型的权重。

模型比较：首先不使用任何训练的模型（即随机选择动作）评估环境，
然后使用训练好的DDPG模型评估环境，最后比较这两种策略的性能」

- - - - - - - - - - - - - - -
尽量最简单的往论文靠 ddpg才是重点
# ---- end of requirements ------