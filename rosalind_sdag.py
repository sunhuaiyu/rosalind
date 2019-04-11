# rosalind_sdag
# cycles in a graph

import networkx as nx

lines = open('rosalind_sdag.txt').read().rstrip().split('\n')
n, _m = [int(i) for i in lines[0].split()]
nodes = [i+1 for i in range(n)]
edges = [tuple([int(i) for i in j.split()]) for j in lines[1:]]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)


pred, d = nx.bellman_ford(G, source=1, weight='weight')

result = [str(d.get(n, 'x')) for n in nodes]    
    
print(' '.join(result))
open('rosalind_sdag_sub.txt', 'wt').write(' '.join(result))
