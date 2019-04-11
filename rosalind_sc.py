# rosalind_sc
# cycles in a graph

import networkx as nx

f = open('rosalind_sc.txt')
k = int(f.readline().rstrip())

result = []
for i in range(k):
    s = ''
    while s == '':
        s = f.readline().rstrip()
    n, m = [int(l) for l in s.split()]
    nodes = [i+1 for i in range(n)]
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    
    for j in range(m):
        u, v = [int(l) for l in f.readline().rstrip().split()]
        G.add_edge(u, v)
    
    output = '-1'
    if nx.is_semiconnected(G):
        output = '1'
    
    result.append(output)

  
result = ' '.join(result)
print(result)
open('rosalind_sc_sub.txt', 'wt').write(result)

