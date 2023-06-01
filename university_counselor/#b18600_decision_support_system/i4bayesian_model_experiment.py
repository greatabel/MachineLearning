from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination
# from pgmpy.factors import TabularCPD
from pgmpy.factors.discrete import TabularCPD

from graphviz import Digraph
import i4data_config

'''
1. ，变成context是，根据不同的地铁站（比如选择伦敦大本钟，博物馆等站）的社交网络/本地评价，天气，拥堵情况，推荐结果是是否想游客推荐交通路线是否下车（原来方案保持不变，还是每一种论点的支撑，我们推荐新加）
2. 我增加贝叶斯机器学习 BayesianModel 和我们的预设的地铁附近的景点 location，quality，cost话费等构建 不同的先天分布，然后做机器推断
3. 一个graphviz绘制推断的结构图

4.不光只分析证据支持，同时还考虑社交媒体的评价（句子），还考虑句子之间的相似程度，这块我就上个成 KNN算法"

'''

def showBN(model, save=False):
    '''传入BayesianModel对象，调用graphviz绘制结构图，jupyter中可直接显示'''
    
    node_attr = dict(
     style='filled',
     shape='box',
     align='left',
     fontsize='12',
     ranksep='0.1',
     height='0.2'
    )
    dot = Digraph(node_attr=node_attr, graph_attr=dict(size="12,12"))
    seen = set()
    edges=model.edges()
    for a,b in edges:
        dot.edge(a,b)
    if save:
        dot.view(cleanup=True)
    return dot


# Now first create the model.
# hospital = BayesianModel([('location', 'cost'),
#                             ('quality', 'cost'),
#                             ('cost', 'no_of_people'),
#                             ('location', 'no_of_people')])
hospital = BayesianModel(i4data_config.header)

cpd_location = TabularCPD('location', 2, i4data_config.location_distribute)
cpd_quality = TabularCPD('quality', 3, i4data_config.quality_distribute)
cpd_cost = TabularCPD('cost', 2,
                      [[0.8, 0.6, 0.1, 0.6, 0.6, 0.05],
                       [0.2, 0.4, 0.9, 0.4, 0.4, 0.95]],
                      ['location', 'quality'], [2, 3])
cpd_no_of_people = TabularCPD('no_of_people', 2,
                              [[0.6, 0.8, 0.1, 0.6],
                               [0.4, 0.2, 0.9, 0.4]],
                              ['cost', 'location'], [2, 2])
hospital.add_cpds(cpd_location, cpd_quality,
                    cpd_cost, cpd_no_of_people)
# Creating the inference object of the model
hospital_inference = VariableElimination(hospital)
# Doing simple queries over one or multiple variables.

location_query = hospital_inference.query(variables=['location'])
print('location_query => \n', location_query)

dot = showBN(hospital)
print(dot.source)
# 画图，filename:图片的名称，若无filename，则使用Digraph对象的name，默认会有gv后缀
# directory:图片保存的路径，默认是在当前路径下保存
dot.view(filename="i4entity_derivation_graph")

hospital_inference.query(variables=['location', 'no_of_people'])
# We can also specify the order in which the variables are to be
# eliminated. If not specified pgmpy automatically computes the
# best possible elimination order.
hospital_inference.query(variables=['no_of_people'],
                           elimination_order=['location', 'cost', 'quality'])


hospital_inference.query(variables=['no_of_people'],
                           evidence={'location': 1})
hospital_inference.query(variables=['no_of_people'],
                           evidence={'location': 1, 'quality': 1})
# In this case also we can simply pass the elimination order for
# the variables.
l = hospital_inference.query(variables=['no_of_people'],
                           evidence={'location': 1},
                           elimination_order=['quality', 'cost'])
print('l=', l)