# rosalind_bfs
# connected components

import pandas as pd
import networkx as nx
from networkx.algorithms import single_source_shortest_path_length as path
import io


m = pd.read_csv('rosalind_bfs.txt', header=None, sep=' ')
nodes = m.ix[0, 0]
edges = m.ix[0, 1]
edge_list = m.ix[1:, :].values.tolist()

G = nx.DiGraph()
G.add_nodes_from(range(1, nodes+1))
G.add_edges_from(edge_list)

p = path(G, source=1)

result = array([p.get(i, -1) for i in range(1, nodes+1)]).astype(int)
result.tofile('rosalind_bfs_sub.txt', sep=' ')

