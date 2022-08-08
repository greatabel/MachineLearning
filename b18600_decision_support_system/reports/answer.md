1.Introduction（清楚描述想解决的是什么问题，确定所作系统要实现的目标）
2.Literature Review（重点在结合其他人论文分析有谁做过相关话题，有哪些相关技术可以用，最后根据优缺点我们选择了某种）
3.Background（对于所使用的具体技术的介绍）
PMG Programming
贝叶斯算法
sk-learn 
k-means
可视化的技术
4.System design（怎么设计的，或者就是解释代码的部分）
5.Result（每几步运算得出什么，后面怎么使用，最终通过运算得出了预计人数概率）
6.Evaluation（根据前面的目标测评自己的系统是否有实现，并分析有哪些是自己的不足）」


# ######### answer:
1.
我不知道以前的，以前是部分是以前的。

新增的部分，我们就想写：去地铁站附近的景点哪儿玩，我们数据监测了地点在社交网络出现频率还有一些评论集合（kmean)
然后根据我们对地点的评论数据、出现讨论的次数等数据，根据先天贝叶斯模型和kmean等分析了可能的喜好和出现讨论次数导致的热度
热度只是我们选择的一个评判标准。
也可以选择其他标准，如果想要分析其他的

2.
有很多，也可以单纯分析社交网络的网络结构，根据6度分离理论和社交网络分析，找到最主流的大v意见。
那个就是单纯对社交网络数据集进行社交网络建模和可视化
和我们比优缺点是：更多考虑了社交网络的层次，缺陷是不能今天隐含知识推理
例如：
https://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CMFD&filename=1020061770.nh&dbname=CMFD202002

3.

numpy
pandas
pgmpy==0.1.13
graphviz==0.19.1
sklearn
主要依托于PMG 和机器学习算法


PMG Programming
概率编程的推理过程就是：对问题进行建模，然后利用计算机采样的方法进行自动的贝叶斯推理（Bayesian inference），得出未知参数的概率分布
https://zh.m.wikipedia.org/zh-hans/%E6%A6%82%E7%8E%87%E7%BC%96%E7%A8%8B

贝叶斯算法
https://baike.baidu.com/item/%E8%B4%9D%E5%8F%B6%E6%96%AF%E5%88%86%E7%B1%BB%E7%AE%97%E6%B3%95/7346561

sk-learn
https://zhuanlan.zhihu.com/p/342941676

k-means
https://zhuanlan.zhihu.com/p/78798251

可视化的技术
我们可视化技术主要是matplot和graphviz
Matplotlib是一个Python 2D绘图库，它以多种硬拷贝格式和跨平台的交互式环境生成出版物质量的图形。 Matplotlib可用于Python脚本


4.
i3data_explore.py 主要是数据探索部分的代码
i4bayesian_model_experiment.py 主要是贝叶斯pmg 编程部分
i5sentence_similar.py 主要是kmean部分
这部分具体可以看论文

5.

1.地铁站附近的景点哪儿玩，我们数据监测了地点在社交网络出现频率还有一些评论集合（这部分在dataset/placename.csv)
2. 然后根据我们对地点的评论数据(i5sentence_similar.py)、出现讨论的次数等数据，
3. 根据先天贝叶斯模型和kmean等分析了可能的喜好和出现讨论次数导致的热度(i4bayesian_model_experiment.py)

6.
我们是一个技术原型，选择的热度判断这个也很难评判，这个需要买家或者论文老师自己也想想理由。
我们也许可以这样说：经过其他第三方网站比如facebok/或者yelp等网站 发现的结论和我们类似。 