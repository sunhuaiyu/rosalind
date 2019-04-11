#rosalind_ba3g

import networkx as nx
from itertools import combinations

edges = []
for line in open('rosalind_ba3g.txt'):
    a, b = line.rstrip().split(' -> ')
    a = int(a)
    b = [int(i) for i in b.split(',')]
    for i in b:
        edges.append((a, i))

G = nx.DiGraph(data=edges)

source, sink = None, None
for node in G.nodes_iter():
	indeg, outdeg = G.in_degree(node), G.out_degree(node)
	if indeg == outdeg - 1:
		source = node
		continue
	if outdeg == indeg - 1:
		sink = node
		continue
	if source is not None and sink is not None:
		break

G.add_edge(sink, source)

result = '->'.join([str(i[0]) for i in list(nx.eulerian_circuit(G, source=source))])
print(result)
open('rosalind_ba3g_sub.txt', 'wt').write(result)

    