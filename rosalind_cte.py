# rosalind_cte
# cycles in a graph

import networkx as nx

f = open('rosalind_cte.txt')
k = int(f.readline().rstrip())

result = []
for i in range(k):
    s = ''
    while s == '':
        s = f.readline().rstrip()
    n, m = [int(l) for l in s.split()]
    nodes = list(range(1, n+1))
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    
    u0, v0, w0 = [int(l) for l in f.readline().rstrip().split()]
    for j in range(1, m):
        u, v, w = [int(l) for l in f.readline().rstrip().split()]
        G.add_edge(u, v, weight=w)
        
    output = '-1'
    if nx.has_path(G, v0, u0):
        output = str(nx.shortest_path_length(G, v0, u0, weight='weight') + w0)
    result.append(output)
    
result = ' '.join(result)
print(result)
open('rosalind_cte_sub.txt', 'wt').write(result)

