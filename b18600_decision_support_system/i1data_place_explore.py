import numpy as np  # linear algebra

import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import json

'''
1. ，变成context是，根据不同的地铁站（比如选择伦敦大本钟，博物馆等站）的社交网络/本地评价，天气，拥堵情况，推荐结果是是否想游客推荐交通路线是否下车（原来方案保持不变，还是每一种论点的支撑，我们推荐新加）
2. 我增加贝叶斯机器学习 BayesianModel 和我们的预设的地铁附近的景点 location，quality，cost话费等构建 不同的先天分布，然后做机器推断
3. 做一个graphviz绘制推断的结构图

4.不光只分析证据支持，同时还考虑社交媒体的评价（句子），还考虑句子之间的相似程度，这块我就上个成 KNN算法"

'''

print("---- 1. let us check the first document in the dataset ----")
df = pd.read_csv("datasets/passenger_dirty.csv")
print(df.head())


doc_text_words = df["PlaceName"].apply(lambda x: len(x.split(" ")))
plt.figure(figsize=(12, 6))
sns.distplot(doc_text_words.values, kde=True, hist=False).set_title(
    "Distribution of text word count of all PlaceName"
)
plt.show()
# plt.savefig("reports/i1.png")
