# rosalind_sq
# cycles in a graph

import networkx as nx
from itertools import combinations

f = open('rosalind_sq.txt')
k = int(f.readline().rstrip())

result = []
for i in range(k):
    s = ''
    while s == '':
        s = f.readline().rstrip()
    n, m = [int(l) for l in s.split()]
    nodes = [i+1 for i in range(n)]
    G = nx.Graph()
    G.add_nodes_from(nodes)
    
    for j in range(m):
        u, v = [int(l) for l in f.readline().rstrip().split()]
        G.add_edge(u, v)
    
    output = '-1'
    tri = []
    for c in nx.cycle_basis(G):
        if len(c) == 4:
            output = '1'
            break
        elif len(c) == 3:
            tri.append(set(c))
    
    if output == '-1' and len(tri) > 1:
        for i in combinations(tri, 2):
            if len(set.intersection(*i)) == 2:
                output = '1'
                break
           
    result.append(output)

result = ' '.join(result)
print(result)
open('rosalind_sq_sub.txt', 'wt').write(result)

