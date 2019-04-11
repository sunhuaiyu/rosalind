#rosalind_ba3h

import networkx as nx
from itertools import combinations


edges = []
f = open('rosalind_ba3h.txt')
k = int(f.readline().rstrip())
for i in f.readlines():
    s = i.rstrip()
    edges.append((s[:-1], s[1:]))

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

result = ''.join([i[0][0] for i in list(nx.eulerian_circuit(G, source=source))])
result += sink[1:]
print(result)
open('rosalind_ba3h_sub.txt', 'wt').write(result)

    