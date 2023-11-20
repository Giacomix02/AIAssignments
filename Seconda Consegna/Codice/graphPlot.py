import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    _pos: dict
    _g: nx.Graph
    _visitati = []
    _individuati = []


    def __init__(self):
        plt.figure("Graph")
        g = nx.Graph()
        self._g = g

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
        nodes_to_remove = [26, 27, 28, 29, 30, 33, 42, 46]
        g.remove_nodes_from(nodes_to_remove)

        # pos = {node: (node % 8, node // 8) for node in g.nodes()}      #normale
        # pos = {node: (7 - node % 8, node // 8) for node in g.nodes()}  #specchiato x
        pos = {node: (node % 8, 7 - node // 8) for node in g.nodes()}
        self._pos = pos

        nx.draw(g, pos=pos, with_labels=True, node_size=300, node_color='skyblue', font_weight='bold', font_size=8,
                edge_color='black')
        nx.draw_networkx_nodes(g, pos=pos, nodelist=[18], node_color='green', node_size=300)
        nx.draw_networkx_nodes(g, pos=pos, nodelist=[43], node_color='red', node_size=300)

    # def printGraph(self):
    #     plt.figure("Graph")
    #     g = nx.Graph()
    #     self._g = g
    #
    #     # Aggiungi i nodi
    #     for i in range(0, 8):
    #         for j in range(0, 8):
    #             g.add_node(i * 8 + j)
    #
    #     # Aggiungi gli archi orizzontali
    #     for i in range(0, 8):
    #         for j in range(0, 7):
    #             g.add_edge(i * 8 + j, i * 8 + j + 1)
    #
    #     # Aggiungi gli archi verticali
    #     for i in range(0, 7):
    #         for j in range(0, 8):
    #             g.add_edge(i * 8 + j, (i + 1) * 8 + j)
    #
    #     # Rimuovi alcuni nodi per formare un quadrato
    #     nodes_to_remove = [26, 27, 28, 29, 30, 33, 42, 46]
    #     g.remove_nodes_from(nodes_to_remove)
    #
    #     # pos = {node: (node % 8, node // 8) for node in g.nodes()}      #normale
    #     # pos = {node: (7 - node % 8, node // 8) for node in g.nodes()}  #specchiato x
    #     pos = {node: (node % 8, 7 - node // 8) for node in g.nodes()}
    #     self._pos = pos
    #
    #     nx.draw(g, pos=pos, with_labels=True, node_size=300, node_color='skyblue', font_weight='bold', font_size=8,
    #             edge_color='black')
    #     nx.draw_networkx_nodes(g, pos=pos, nodelist=[18], node_color='green', node_size=300)
    #     nx.draw_networkx_nodes(g, pos=pos, nodelist=[43], node_color='red', node_size=300)

    def colora(self, rettangolo):
        if rettangolo.is_visitato():
            self._visitati.insert(rettangolo.get_numero(), rettangolo.get_numero())
                    
        elif rettangolo.is_individuato():
            self._individuati.insert(rettangolo.get_numero(), rettangolo.get_numero())
        
        nx.draw_networkx_nodes(self._g, pos=self._pos, nodelist=self._individuati, node_color='grey', node_size=300)
        nx.draw_networkx_nodes(self._g, pos=self._pos, nodelist=self._visitati, node_color='green', node_size=300)
