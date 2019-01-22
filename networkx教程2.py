# python
# -*- coding:utf-8 -*-
# author liao_wk time
import networkx as nx
import matplotlib.pyplot as plt


plt.figure(figsize=(8, 10))
G = nx.Graph()
edlist = [(1, 2), (2, 3), (3, 4), (4, 1), ('a', 2)]
G.add_edges_from(edlist)
edlist = [('a', 'b', 1.0), ('c', 'd', 2.0), ('a', 'c', 3.0)]
G.add_weighted_edges_from(edlist)
G.add_edge('a', 'c', weight=2.0)
plt.subplot(121)
nx.draw(G)
G1 = nx.Graph()
G1.add_edge(77, 78, color='red', weight=0.84, size=300)
print(78 in G1)
print(G1[77][78])   # 获得边1，2的属性。
print(G1.edges[77, 78])   # 获得边1，2的属性。
plt.subplot(122)
nx.draw(G1)
plt.show()
