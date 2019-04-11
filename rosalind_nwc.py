# rosalind_sq
# cycles in a graph

import networkx as nx
from itertools import combinations

f = open('rosalind_nwc.txt')
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
    
    edges = [(int(l) for l in f.readline().rstrip().split()) for j in range(m)]
    G.add_weighted_edges_from(edges)
    
    output = '-1'
    if nx.negative_edge_cycle(G, weight='weight'):
        output = '1'       
    result.append(output)

result = ' '.join(result)
print(result)
open('rosalind_nwc_sub.txt', 'wt').write(result)

