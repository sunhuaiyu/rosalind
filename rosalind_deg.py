# sun.huaiyu
# DEG

import networkx as nx

G = nx.Graph()
f = open('rosalind_deg.txt')
header = f.readline()
for line in f:
    G.add_edge(*[int(i) for i in line.split()])
f.close()

f = open('rosalind_deg_ans.txt', 'wt')
f.write(' '.join([str(G.degree(i)) for i in G.nodes()]))
f.close()
