#Example1
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
 
g = nx.Graph()

#rows
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)


nx.draw_planar(g, with_labels = True)
plt.savefig("filename.png")






#Example2
# importing networkx 
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt
 
g = nx.Graph()
 
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(1, 4)
g.add_edge(1, 5)
 
nx.draw(g, with_labels = True)
#plt.savefig("filename.png")




#

# #Example7
# import networkx as nx
# import matplotlib.pyplot as plt
# G = nx.DiGraph()
#
# G.add_edge('ts','mail',weight=6)
# G.add_edge('mail','ts',weight=6)
# G.add_edge('o103','ts',weight=8)
# G.add_edge('ts','o103',weight=8)
# G.add_edge('o103','b3',weight=4)
# G.add_edge('o103','o109',weight=12)
# G.add_edge('o109','o103',weight=12)
# G.add_edge('o109','o119',weight=16)
# G.add_edge('o119','o109',weight=16)
# G.add_edge('o109','o111',weight=4)
# G.add_edge('o111','o109',weight=4),
# G.add_edge('b1','c2',weight=3)
# G.add_edge('b1','b2',weight=6)
# G.add_edge('b2','b1',weight=6),
# G.add_edge('b2','b4',weight=3)
# G.add_edge('b4','b2',weight=3),
# G.add_edge('b3','b1',weight=4)
# G.add_edge('b1','b3',weight=4),
# G.add_edge('b3','b4',weight=7)
# G.add_edge('b4','b3',weight=7),
# G.add_edge('b4','o109',weight=7)
# G.add_edge('c1','c3',weight=8)
# G.add_edge('c3','c1',weight=8),
# G.add_edge('c2','c3',weight=6)
# G.add_edge('c3','c2',weight=6),
# G.add_edge('c2','c1',weight=4)
# G.add_edge('c1','c2',weight=4),
# G.add_edge('o123','o125',weight=4)
# G.add_edge('o125','o123',weight=4),
# G.add_edge('o123','r123',weight=4)
# G.add_edge('r123','o123',weight=4),
# G.add_edge('o119','o123',weight=9)
# G.add_edge('o123','o119',weight=9),
# G.add_edge('o119','storage',weight=7)
# G.add_edge('storage','o119',weight=7)
#
# import pygraphviz
# #pos = nx.random_layout(G,dim=7,seed=7)
# #pos=nx.circular_layout(G,scale=14)
# #if you choose to use this layout, you have to install pygraphviz
# #!apt install libgraphviz-dev
# #!pip install pygraphviz
# pos = nx.nx_agraph.graphviz_layout(G,prog='neato')
# #pos = nx.spring_layout(G, seed=7,scale=10)  # positions for all nodes - seed for reproducibility
# nx.draw_networkx_nodes(G,pos,node_size=500)
# edgeslist = [(u, v) for (u, v, d) in G.edges(data=True)]
# nx.draw_networkx_edges(G, pos,edgelist=edgeslist, width=2)
# # node labels
# nx.draw_networkx_labels(G, pos, font_size=8, font_family="sans-serif")
# # edge weight labels
# edge_labels = nx.get_edge_attributes(G, "weight")
# nx.draw_networkx_edge_labels(G, pos, edge_labels)
#
#
# ax = plt.gca()
# plt.axis("off")
# #plt.figure(G, figsize=(30,30))
# plt.show()
# #plt.figure(figsize =(9, 9))
# #nx.draw_networkx(G)

