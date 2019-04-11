# rosalind_dag
# cycles in a graph

import networkx as nx
from networkx.algorithms.dag import topological_sort

lines = open('rosalind_ts.txt').read().rstrip().split('\n')
n, _m = [int(i) for i in lines[0].split()]
nodes = [i+1 for i in range(n)]
edges = [tuple([int(i) for i in j.split()]) for j in lines[1:]]

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

result = ' '.join([str(i) for i in topological_sort(G)])

print(result)
open('rosalind_ts_sub.txt', 'wt').write(result)
