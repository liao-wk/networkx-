# python
# -*- coding:utf-8 -*-
# author liao_wk time
import networkx as nx
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 8))
G = nx.Graph()
G.add_node(1)
G.add_edge(2, 3)
H = nx.path_graph(10)
G.add_nodes_from(H)
e = [20, 30]
G.add_edge(*e)  # 不能缺少*
G.add_weighted_edges_from([('y', 'x', 3.0)])
G.add_edges_from([(1, 2), (2, 3)])
print(H.edges)
G.add_edges_from(H.edges)
G.add_node("spam")
G.add_nodes_from("spam")
#  G.clear()  # 清除上面的节点和边
print(G.number_of_nodes())
print(G.number_of_edges())
print(G.node)
print(dict(G.nodes))
print(list(G.nodes))
print(dict(G.degree))  # 输出一个字典，字典的键是度。
print(G.degree)  # 输出一个含有元组的列表，元组的第一个是节点，第2个是对应的度。
nx.draw_networkx(G)
plt.show()
