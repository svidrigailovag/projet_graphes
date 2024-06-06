import networkx as nx
import random as rd
import matplotlib.pyplot as plt
n1, n2, n3, N, p = 3, 5, 3, 5, 0.5

def random_multipartite_graph(n1 : int, n2 : int, n3 : int, N : int, p : float):
    "Generates a random multipartite graph with n1 producers, n2 switches in each layer, n3 clients, N layers of switches, and p probability to have an edge between two consecutive layers"
##Nodes    
    G = nx.Graph()
    P = list(range(n1))
    G.add_nodes_from(P, layer = 'P') #producers layer
    for i in range(N): #switches layers
        S = list(range(n1 + i*n2, n1 + (i+1)*n2))
        G.add_nodes_from(S, layer = f'S{i}')
    C = list(range(n1 + N*n2, n1 + N*n2 + n3))
    G.add_nodes_from(C, layer = 'C')

#Edges
    classes = ['P']+[f'S{i}' for i in range(N)]+['C']
    for L in range(len(classes)-1):
        for u in [nodes for nodes in G.nodes() if G.nodes[nodes]['layer'] == classes[L]]:
            for v in [nodes for nodes in G.nodes() if G.nodes[nodes]['layer'] == classes[L+1]]:
                a = rd.random()
                if a < p: G.add_edge(u, v)
    
    return G

def layout_color(G):
    C = ['red']+N*['blue']+['green']
    pos, color = dict(), list()
    classes = ['P']+[f'S{i}' for i in range(N)]+['C']
    offset = [0]+[n1+i*n2 for i in range(N)]+[n1+N*n2]
    for i in range(len(classes)):
        for node in [nodes for nodes in G.nodes() if G.nodes[nodes]['layer'] == classes[i]]:
            pos[node] = (node-offset[i], N+1-i)
            color.append(C[i])
        
    return pos, color



