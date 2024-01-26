# Reinforcement Learning An Introduction Second Edition
Richard S. Sutton

# 但在1979年我们就开始意识到，那些一直以来被人视为理所当然的最简单的想法，
从计算角度来看，受到的关注实在寥寥。那就是关于一个学习系统最简单的思想，
即学习系统总是有某些需要，它总是通过调整自身的行为来最大化其所在环境给出的一些特殊信号。 
这就是“ 享乐主义” 学习系统的概念，或者如我们现在所说，强化学习的概念
-----
（#在心理学中，享乐主义理论认为个体的行为主要是为了追求快乐和避免痛苦。
在强化学习的背景下，这种理论被转化为算法和机制，其中“快乐”或“满足感”通常由数值化的奖励来表示。）

例如，在训练一个强化学习算法控制的机器人时，当机器人执行正确的动作时，它会收到正奖励（类似于快乐），
而错误的动作会得到负奖励或没有奖励（类似于痛苦或不满足）


1.1

# 强化学习就是学习“做什么(即如何把当前的情境映射成动作)才能使得数值化的收益信号最大化”
学习者不会被告知应该采取什么动作，而是必须自己通过尝试去发现哪些动作会产生最丰厚的收益。
在最有趣又最困难的案例中，动作往往影响的不仅仅是即时收益，也会影响下一个情境，从而影响随后的收益。
这两个特征:试错和延迟收益 是强化学习两个最重要最显著的特征

@ 强化学习和现在机器学习领域中广泛使用的有监督学习不同，有监督学习是从外部监督者提供的带标注训练集中进行学习。
每一个样本都是关于情境和标注的描述。所谓标注，即针对当前情境，系统应该做出的正确动作，也可将其看作对当前情景进行分类的所属类别标签。
采用这种学习方式是为了让系统能够具备推断或泛化能力，能够响应不同的情境并做出正确的动作，哪怕这个情境并没有在训练集合中出现过。
这是一种重要的学习方式，但是并不适用于从交互中学习这类问题。

在交互问题中，我们不可能获得在所有情境下既正确又有代表性的动作示例。在一个未知领域，
若想做到最好 (收益最大) 智能体必须要能够从自身的经验中学习

@，无监督学习是一个典型的寻找未标注数据中隐含结构的过程。看上去所有的机器学习范式都可以被划分成有监督学习和无监督学习，但事实并非如此。尽管有人可能会认为强化学习也是一种无监督学习，因为它不依赖于每个样本所对应的正确行为 (即标注 )，但强化学习的目的是最大化收益信号，而不是找出数据的隐含结构。通过智能体的经验揭示其结构在强化学习中当然是有益的，但这并不能解决最大化收益信号的强化学习问题。
因此，我们认为强化学习是与有监督学习和无监督学习并列的第三种机器学习范式，当然也有可能存在其他的范式

（#监督学习就像有老师在旁边指导你；
无监督学习就像自己探索和发现；
而强化学习则像是通过游戏的奖励和惩罚来学习如何更好地玩游戏）


# 强化学习带来了一个独有的挑战 — — “ 试探 ” 与 “ 开发 ” 之间的折中权衡。
为了获得大量的收益，强化学习智能体一定会更喜欢那些在过去为它有效产生过收益的动作。
但为了发现这些动作，往往需要尝试从来选择过的动作。智能体必须开发已有的经验来获取收益，同时也要进行试探，
使得未来可以获得更好的动作选择空间。于是两难情况产生了:无论是试探还是开发，都不能在完全没有失败的情况下进行
智能体必须尝试各种各样的动作，并且逐渐地筛选出那些最好的动作。在一个随机任务中，为了获得对收益期望的可靠估计，
需要对每个动作多次尝试。这个“ 试探-开发” 困境问题已经被数学家们深入研究了几十年，但是仍然没有解决。
而就目前而言，在有监督学习和无监督学习中，至少在最简单的形式中，并不存在权衡试探和开发的问题
（#最好翻译成 试探和利用; 
#因为环境是千变万化的，可能没有银弹，不一定存在万能的强化方法，也许只有个大概策略
#人类在这个资源不是无限的世界（至少表面上，比如时间和精力），怎么平衡长远和当下等，何尝也没找到万能最佳策略）

1.3

# 除了智能体和环境之外，强化学习系统有四个核心要素:策略、收益信号、价值函数以及(可选的)对环境建立的模型



---------------------------

强化学习与其他机器学习方法最大的不同，就在于前者的训练信号是用来评估给定动作的好坏的，而不是通过给出正确动作范例来进行直接的指导。这使得主动地反复试验以试探出好的动作变得很有必要。单纯的“评估性反馈”只能表明当前采取的动作的好坏程度，但却无法确定当前采取的动作是不是所有可能性中最好的或者最差的。另一方面，单纯的“指导性反馈”表示的是应该选择的正确动作是什么，并且这个正确动作和当前实际采取的动作无关，这是有监督学习的基本方式，其被广泛应用于模式分类 、 人工神经网络和系统辨识等。上述两种不同的反馈有着很大的不同:评估性反馈依赖于当前采取的动作，即采取不同的动作会得到不同的反馈;而指导性反馈则不依赖于当前采取的动作，即采取不同的动作也会得到相同的反馈。当然，也有将两者结合起来的情况
























