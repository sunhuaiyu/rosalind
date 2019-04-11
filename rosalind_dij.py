# rosalind_dij
# shortest path

import pandas as pd
import networkx as nx
from networkx.algorithms import single_source_dijkstra_path_length as path


m = pd.read_csv('rosalind_dij.txt', header=None, sep=' ', names=['a', 'b', 'c'])
nodes = int(m.ix[0, 0])
edges = int(m.ix[0, 1])
edge_list = m.ix[1:, :].values

G = nx.DiGraph()
G.add_nodes_from(range(1, nodes+1))
G.add_weighted_edges_from(edge_list)

p = path(G, source=1)

result = array([p.get(i, -1) for i in range(1, nodes+1)]).astype(int)
result.tofile('rosalind_dij_sub.txt', sep=' ')

