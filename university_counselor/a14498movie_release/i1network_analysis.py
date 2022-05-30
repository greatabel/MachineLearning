# coding:utf-8
import matplotlib.pyplot as plt
import networkx as nx
import numpy
import numpy as np
import json
from ast import literal_eval

# 自行替换
file_path = "i1SGScrapy/downloads/nezha_processed.csv"
# file_path = "i1SGScrapy/downloads/wandering_earth_processed.csv"
with open(file_path, "r") as f:
    rt_time = []
    for line in f:
        # print(line, '#'*20)
        items = line.strip().split("\t")
        print(items)
        time = items[2]
        # print time
        # day = time[1:5] + time[6:8] + time[9:11]
        day = items[3].replace("-", "")
        # print day
        hm = items[4].replace(":", "")
        # hms= time[9:17].replace(':', '')
        # hm = time[12:17].replace(":", "")
        # time = int(day + hm)
        if hm != 'time':
            time = int(hm)

            rt_time.append(time)
print(rt_time, '@'*10)
# time.sleep(10)
# 计算转发时间的先后顺序
array = numpy.array(rt_time)
order = array.argsort()
ranks = order.argsort()

G = nx.Graph()
with open(file_path, "r") as f:
    for position, line in enumerate(f):
        items = line.strip().split("\t")


        uid = items[6]
        obj = items[-1]
        rtuid = items[-6]
        print('obj=', obj, type(obj))
        if obj is not None and obj!= 'trans_dest':
            obj = literal_eval(obj)
            print('obj====', obj, type(obj))
            if len(obj) >= 1:
                if not isinstance(obj[0], str):
                    rtuid = obj[0]['id']
                    print('#'*20, rtuid)
            # rtuid = items[-6]
                    print('uid=', uid, 'rtuid=',rtuid)

        G.add_edge(uid, rtuid, time=ranks[position])
edges, colors = zip(*nx.get_edge_attributes(G, "time").items())

print("-" * 10)
# degree=G.degree()#计算节点的出度
# degree=G.degree()#计算节点的出度
degree = G.degree(G)
closenesss = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)

print(G.number_of_edges())  # 1547
# print g.diameter(G) # 2
path_length = nx.all_pairs_shortest_path_length(G)
pos = nx.spring_layout(G)  # 设置网络的布局
# fig = plt.figure(figsize=(80, 60),facecolor='white')
# pos=nx.spring_layout(G) #设置网络的布局


de = dict(G.degree)
de2 = [de[v] for v in de.keys()]
# print("de2",de2)
nx.draw_networkx(
    G,
    pos,
    node_size=de2,
    with_labels=False,
    node_color="red",
    linewidths=None,
    width=1.0,
    edge_color="blue",
)

plt.savefig("nezha_shortime.png")
plt.show()
'''
[115755.6, 337819.4, 888868.8, 363432.8, 2270.8, 63301.8] ##############################
6 6 @@@@@@@@@@
- *- *- *- *- *
            2
-7.954e+04 x + 3.464e+05 x + 1.583e+05
- *- *- *- *- *

#################### myerror= 204025.03551115654
'''