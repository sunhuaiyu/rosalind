# rosalind_hdag
# cycles in a graph

import networkx as nx
from networkx.algorithms.dag import dag_longest_path

f = open('rosalind_hdag.txt')
k = int(f.readline().rstrip())

result = []
for i in range(k):
    
    n, m = [int(l) for l in f.readline().rstrip().split()]
    nodes = [i+1 for i in range(n)]
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    
    for j in range(m):
        u, v = [int(l) for l in f.readline().rstrip().split()]
        G.add_edge(u, v)
    
    output = '-1'
    try:
        path = dag_longest_path(G)
        if len(path) == n:
            output = '1 ' + ' '.join([str(i) for i in path])
    except:
        pass
    result.append(output)

    
result = '\n'.join(result)
print(result)
open('rosalind_hdag_sub.txt', 'wt').write(result)

