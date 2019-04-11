# sun.huaiyu
# DDEG

import networkx as nx

G = nx.Graph()
f = open('rosalind_ddeg.txt')
n_nodes, n_edges = [int(i) for i in f.readline().split()]
edges =[[int(i) for i in line.split()] for line in f]
f.close()

G.add_nodes_from(range(1, n_nodes+1))
G.add_edges_from(edges)

f = open('rosalind_ddeg_ans.txt', 'wt')
f.write(' '.join([str(sum([G.degree(i) for i in G.neighbors(k)])) for k in G.nodes()]))
f.close()
