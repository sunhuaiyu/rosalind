# rosalind_tree
# tree of life

import pandas as pd
import networkx as nx

m = pd.read_csv('rosalind_tree.txt', sep=' ', header=None, names=['a', 'b'])

edge_list = m.ix[1:, :].astype(int).values.tolist()
nodes = m.ix[0, 0].astype(int)

G = nx.Graph()
G.add_nodes_from(range(1, nodes+1))
G.add_edges_from(edge_list)

n = len(list(nx.connected_component_subgraphs(G)))
print(n - 1)

