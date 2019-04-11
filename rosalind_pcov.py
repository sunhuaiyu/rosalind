#rosalind_pcov

import networkx as nx


# create de Bruijn graph
G = nx.DiGraph()
for l in open('rosalind_pcov.txt'):
    u = l.rstrip()
    G.add_edge(u[:-1], u[1:], label=u)

result = ''
for edge in nx.find_cycle(G):
    result += edge[0][0]

print(result)
open('rosalind_pcov_sub.txt', 'wt').write(result)

