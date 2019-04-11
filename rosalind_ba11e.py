#rosalind_ba11e
'''
Peptide Sequencing Problem:
Given a spectral vector S, find a peptide vector with maximum score against S.

Given: A space-delimited spectral vector S.

Return: A peptide with maximum score against S. 
For masses with more than one amino acid, any choice may be used.
'''
import numpy as np
import networkx as nx

mass_aa = {71: 'A', 103: 'C', 129: 'E', 115: 'D', 57: 'G', 147: 'F', 
 113: 'I', 137: 'H', 128: 'K', 131: 'M', 114: 'N', 97: 'P', 87: 'S', 
 156: 'R', 101: 'T', 186: 'W', 99: 'V', 163: 'Y'} #, 4: 'X', 5: 'Z'}

spec = np.array(['0'] + open('rosalind_ba11e.txt').readline().rstrip().split(), dtype=int)
m = len(spec)

G = nx.DiGraph()
G.add_nodes_from(range(m))

# use sign-reversed weight of the target node for each edge weight
for i in range(m-1):
    for j in range(i+1, m):
        d = j - i 
        if d in mass_aa.keys():
            G.add_edge(i, j, {'weight': -spec[j], 'label': mass_aa[d]})


# A Belllman_ford search and reconstruction to find
# the shortest path (i.e. maximal -Score) in the graph with sign-reversed weights 
v = m-1
path = nx.bellman_ford(G, 0)[0]


result = ''
u = path[v]
while u != None:
    result = G[u][v]['label'] + result
    v = u
    u = path[v]

print(result)
