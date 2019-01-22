# python
# -*- coding:utf-8 -*-
# author liao_wk time
import networkx as nx
import matplotlib.pyplot as plt

G = nx.cubical_graph()
plt.subplot(121)
nx.draw(G)
plt.subplot(122)
nx.draw(G, pos=nx.circular_layout(G), node_color='g', edge_color='b')
plt.show()
