import networkx as nx
from graphes import random_multipartite_graph, layout_color, n1, n2, n3, N, p
import matplotlib.pyplot as plt


def draw_graph(n1 : int, n2 : int, n3 : int, N : int, p : float):
    G = random_multipartite_graph(n1, n2, n3, N, p)
    pos, node_color = layout_color(G)
    nx.draw(G, pos=pos, node_color=node_color, node_size=500)
    plt.show()


if __name__ == '__main__':
    draw_graph(n1, n2, n3, N, p)