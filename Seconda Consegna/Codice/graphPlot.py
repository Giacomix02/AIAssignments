# import networkx as nx
# import matplotlib.pyplot as plt
#
#
# def printGraph():
#
#     plt.figure()
#     g = nx.Graph()
#
#     x = 0
#
#     for i in range(0, 8):  # rows
#         for j in range(0, 8):
#             if x % 7 != 0:
#                 g.add_edge(x, x + 1)
#             x += 1
#
#     x = 0
#
#     for i in range(0, 8):  # columns
#         for j in range(0, 8):
#             if x + 8 < 64:
#                 g.add_edge(x, x + 8)
#             x += 1
#
#     g.remove_node(26)
#     g.remove_node(27)
#     g.remove_node(28)
#     g.remove_node(29)
#     g.remove_node(30)
#     g.remove_node(33)
#     g.remove_node(42)
#     g.remove_node(46)
#
#     nx.draw_planar(g, with_labels=True)

import networkx as nx
import matplotlib.pyplot as plt

def printGraph():
    plt.figure()
    g = nx.Graph()

    # Aggiungi i nodi
    for i in range(0, 8):
        for j in range(0, 8):
            g.add_node(i * 8 + j)

    # Aggiungi gli archi orizzontali
    for i in range(0, 8):
        for j in range(0, 7):
            g.add_edge(i * 8 + j, i * 8 + j + 1)

    # Aggiungi gli archi verticali
    for i in range(0, 7):
        for j in range(0, 8):
            g.add_edge(i * 8 + j, (i + 1) * 8 + j)

    # Rimuovi alcuni nodi per formare un quadrato
    nodes_to_remove = [26,27,28,29,30,33,42,46]
    g.remove_nodes_from(nodes_to_remove)

    #pos = {node: (node % 8, node // 8) for node in g.nodes()}      #normale
    #pos = {node: (7 - node % 8, node // 8) for node in g.nodes()}  #specchiato x
    pos = {node: (node % 8, 7 - node // 8) for node in g.nodes()}

    nx.draw(g, pos=pos, with_labels=True, node_size=300, node_color='skyblue', font_weight='bold', font_size=8, edge_color='black')
    nx.draw_networkx_nodes(g, pos=pos, nodelist=[18], node_color='green', node_size=300)
    nx.draw_networkx_nodes(g, pos=pos, nodelist=[43], node_color='red', node_size=300)
