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
python3 i1main.py









# ---- start of requirements ------


将强化学习与多目标粒子群优化（MOPSO）算法结合以解决考虑新能源的机组组合问题。
目标函数考虑了各种因素，包括火电机组成本、碳排放成本、风险价值以及新能源消纳量。
或许要新能源机组的出力上下限作为约束条件。

通过预测负荷值和风速数据作为输入信息，
通过强化学习和MOPSO技术寻找火电机组和风电机组的最优调度决策
在满足出力上下限约束的前提下,
同时追求成本的最小化，风险的降低以及新能源消纳量的最大化

pdf是一个复杂的多目标优化问题，通过强化学习和粒子群优化这两种智能优化方法，
与传统的MOPSO进行了对比。实验结果以图形形式展示（Cost，risk，Renewable Consumption）
以更直观地呈现我们算法的性能。我们没有涉及非参数估计、带宽和卡方的内容，
也没有涉及带宽机制的对比，这些都是为了专注于主要的优化目标和方法。


# ---- end of requirements ------