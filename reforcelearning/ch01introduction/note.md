强化学习系统2个关键元素：

rewrard： 学习目标，学习者在行动后收到环境发来的奖励。
policy:   根据不同观测决定采用不同动作，观测到动作就是策略


强化学习问题用Agent-Environment Interface研究
agent： 强化学习中的决策者和学习者，可以作出决策和接受奖励信号
		我们并不需要对智能体本身建模，只需要了解它在不同环境下可以作出的动作，并接受奖励信号
environment： 强化系统中除agent外所有事物。


agent 和 environment交互主要3个环节:
智能体观测环境，活动环境的oberservation, O
智能体根据观测作出决策，对环境施加的动作action ,A
环境受智能体影响，改变自己状态states,S， 并给出奖励reward，R

