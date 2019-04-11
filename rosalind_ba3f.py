#rosalind_ba3f

import networkx as nx


edges = []
for line in open('rosalind_ba3f.txt'):
    a, b = line.rstrip().split(' -> ')
    a = int(a)
    b = [int(i) for i in b.split(',')]
    for i in b:
        edges.append((a, i))

G = nx.DiGraph(data=edges)

eu_c = list(nx.eulerian_circuit(G))

result = '->'.join([str(i[0]) for i in eu_c] + [str(eu_c[0][0])])
print(result)
open('rosalind_ba3f_sub.txt', 'wt').write(result)

    