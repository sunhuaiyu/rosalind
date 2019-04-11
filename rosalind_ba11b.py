# rosalind_ba11b
import numpy as np
import networkx as nx
from itertools import permutations

aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
 'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163, 'X': 4, 'Z': 5}

mass_aa = {71: 'A', 103: 'C', 129: 'E', 115: 'D', 57: 'G', 147: 'F', 
 113: 'I', 137: 'H', 128: 'K', 131: 'M', 114: 'N', 97: 'P', 87: 'S', 
 156: 'R', 101: 'T', 186: 'W', 99: 'V', 163: 'Y', 4: 'X', 5: 'Z'}

def spectrum2edges(spec):
    '''spec is a sorted list'''
    n = len(spec)
    edges = []
    for i in range(n-1):
        for j in range(i+1, n):
            d = spec[j] - spec[i]
            if (spec[j] - spec[i]) in mass_aa.keys():
                edges.append((i, j, mass_aa[d]))    
    return edges
    
spec = sorted([int(i) for i in 
              open('rosalind_ba11b.txt').readline().rstrip().split()] 
              + [0])
n = len(spec)

G = nx.DiGraph()
G.add_nodes_from(range(n))

for i in spectrum2edges(spec):
    G.add_edge(i[0], i[1], label=i[2])

result = ''
for i, j in permutations(range(n), 2):
    for path in nx.all_simple_paths(G, i, j):
        peptide = ''.join([G[u][v]['label'] for u, v in zip(path[:-1], path[1:])])
        prefix = [peptide[:k] for k in range(1, len(peptide))] 
        suffix = [peptide[k:] for k in range(1, len(peptide))]
        full_spec = sorted([sum([aa_mass[k] for k in p]) 
                           for p in prefix + suffix + [peptide]] + [0])
        if full_spec == spec:
            result = peptide
            break
    if result != '':
        break

open('rosalind_ba11b_sub.txt', 'wt').write(result)
print(result)



