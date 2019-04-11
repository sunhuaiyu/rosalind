# rosalind_scc
# cycles in a graph

import networkx as nx
from networkx.algorithms.components import number_strongly_connected_components

lines = open('rosalind_scc.txt').read().rstrip().split('\n')
n, _m = [int(i) for i in lines[0].split()]
nodes = [i+1 for i in range(n)]
edges = [tuple([int(i) for i in j.split()]) for j in lines[1:]]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

print(number_strongly_connected_components(G))
