# rosalind_sdag
# cycles in a graph

import networkx as nx
from networkx.algorithms import shortest_path_length

lines = open('rosalind_bf.txt').read().rstrip().split('\n')
n, _m = [int(i) for i in lines[0].split()]
nodes = [i+1 for i in range(n)]
edges = [tuple([int(i) for i in j.split()]) for j in lines[1:]]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)

result = []
for i in nodes:
    try:
        l = shortest_path_length(G, source=1, target=i, weight='weight')
        result.append(str(l))
    except:
        result.append('x')

print(' '.join(result))
open('rosalind_bf_sub.txt', 'wt').write(' '.join(result))
