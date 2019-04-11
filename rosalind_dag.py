# rosalind_dag
# cycles in a graph

import networkx as nx
from networkx.algorithms.dag import is_directed_acyclic_graph

m = open('rosalind_dag.txt').read().split('\n\n')
k = int(m[0])

result = []
for g in m[1:]:
    lines = g.rstrip().split('\n')
    n, _m = [int(i) for i in lines[0].split()]
    nodes = [i+1 for i in range(n)]
    edges = [tuple([int(i) for i in j.split()]) for j in lines[1:]]
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    if is_directed_acyclic_graph(G):
        output = '1'
    else:
        output = '-1'
    result.append(output)
    

print(' '.join(result))
open('rosalind_dag_sub.txt', 'wt').write(' '.join(result))
