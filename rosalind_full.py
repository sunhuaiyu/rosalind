# rosalind_full
import numpy as np
import networkx as nx
from itertools import permutations

residue = np.array(['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
       'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])
mass = np.array([  71.03711,  103.00919,  115.02694,  129.04259,  147.06841,
         57.02146,  137.05891,  113.08406,  128.09496,  113.08406,
        131.04049,  114.04293,   97.05276,  128.05858,  156.10111,
         87.03203,  101.04768,   99.06841,  186.07931,  163.06333])

a = np.fromfile('rosalind_full.txt', sep='\n')
L = a[0]
spec = np.array(sorted(a[1:]))

# find all b-y ion pairs
n = len(spec)
pairs = []
for i in range(n-1):
    for j in range(i+1, n):
        if abs(spec[i] + spec[j] - L) < 0.0001:
            pairs.append([i, j])

# construct DiGraph, draw edges between two b-y pairs in both directions,
# if their mass difference matching a residue, try both orientations (b-y and y-b)
n = len(pairs)
G = nx.DiGraph()
for i in range(n-1):
    for j in range(i+1, n):    
        for d in (spec[pairs[i][0]] - spec[pairs[j][0]], 
                       spec[pairs[i][0]] - spec[pairs[j][1]]):
            if (abs(mass - abs(d)) < 0.0001).any():
                aa = residue[np.where(abs(mass - abs(d)) < 0.0001)[0][0]]
                G.add_edge(i, j, label=aa)
                G.add_edge(j, i, label=aa)

# reconstruct sequence by finding any simple path of length n
result = ''
for i, j in permutations(range(n), 2):
    for p in nx.all_simple_paths(G, i, j):
        if len(p) == n:
            result = ''.join([G[u][v]['label'] for u, v in zip(p[:-1], p[1:])])
            break
    if result != '':
        break
        
open('rosalind_full_sub.txt', 'wt').write(result)
print(result)