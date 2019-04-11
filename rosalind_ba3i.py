#rosalind_ba3i

import networkx as nx
from itertools import product


edges = []
f = open('rosalind_ba3i.txt')
k = int(f.readline().rstrip())
for i in [''.join(i) for i in product('01', repeat=k)]:
    edges.append((i[:-1], i[1:]))

G = nx.DiGraph(data=edges)

circle = list(nx.eulerian_circuit(G))
result = ''.join([i[0][0] for i in list(nx.eulerian_circuit(G))])

print(result)
open('rosalind_ba3i_sub.txt', 'wt').write(result)

    