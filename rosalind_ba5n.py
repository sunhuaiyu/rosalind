# rosalind_ba5n


import networkx as nx
from networkx.algorithms.dag import topological_sort

G = nx.DiGraph()

for line in open('rosalind_ba5n.txt'):
    i, j = line.rstrip().split(' -> ')
    for k in j.split(','):
        G.add_edge(int(i), int(k))

result = ', '.join([str(i) for i in topological_sort(G)])

print(result)
open('rosalind_ba5n_sub.txt', 'wt').write(result)
