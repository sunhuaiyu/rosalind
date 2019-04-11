#rosalind_ba7a

import networkx as nx
import numpy as np


#read data
f = open('rosalind_ba7a.txt')
n = int(f.readline().rstrip())

G = nx.Graph()
for line in f:
    l = line.rstrip().split('->')
    u  = int(l[0])
    v, w = map(int, l[1].split(':'))
    G.add_edge(u, v, weight=w)

m = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(i, n):
        d = nx.shortest_path_length(G, i, j, weight='weight')
        m[i, j] = d
        m[j, i] = d

result = '\n'.join([' '.join([str(i) for i in rows]) for rows in m]) 
print(result)
open('rosalind_ba7a_sub.txt', 'wt').write(result)