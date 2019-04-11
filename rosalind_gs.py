# rosalind_gs
# cycles in a graph

import networkx as nx

f = open('rosalind_gs.txt')
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
    
    for j in range(m):
        u, v = [int(l) for l in f.readline().rstrip().split()]
        G.add_edge(u, v)
        
    output = '-1'
    for v in nodes:
        if nx.descendants(G, v) | {v} == set(nodes):
            output = str(v)
            break
    result.append(output)
    
result = ' '.join(result)
print(result)
open('rosalind_gs_sub.txt', 'wt').write(result)

