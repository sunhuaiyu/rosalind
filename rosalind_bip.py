# rosalind_cc
# connected components

import pandas as pd
import networkx as nx
from networkx.algorithms import bipartite
import io


file = open('rosalind_bip.txt').read().split('\n\n')

result = ''
for f in file[1:]: 
    m = pd.DataFrame([i.split() for i in f.rstrip().split('\n')]).astype(int)

    nodes = m.ix[0, 0]
    edges = m.ix[0, 1]
    edge_list = m.ix[1:, :].values.tolist()

    G = nx.Graph()
    G.add_nodes_from(range(1, nodes+1))
    G.add_edges_from(edge_list)

    if bipartite.is_bipartite(G):
        result += '1 '
    else:
        result += '-1 '

print(result)

