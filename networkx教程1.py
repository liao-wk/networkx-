# python
# -*- coding:utf-8 -*-
# author liao_wk time
import networkx as nx
import matplotlib.pyplot as plt
import math

plt.figure(figsize=(8, 10))
G = nx.Graph()
G.add_edge(1, 2)
G.add_edge(2, 3, weight=0.9)
G.add_edge('y', 'x', function=math.cos)
G.add_node(math.cos)
nx.draw_networkx(G)
plt.show()
