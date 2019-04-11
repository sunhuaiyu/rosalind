# rosalind_sgra
import numpy as np
import networkx as nx

residue = np.array(['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
       'Q', 'R', 'S', 'T', 'V', 'W', 'Y'])
mass = np.array([  71.03711,  103.00919,  115.02694,  129.04259,  147.06841,
         57.02146,  137.05891,  113.08406,  128.09496,  113.08406,
        131.04049,  114.04293,   97.05276,  128.05858,  156.10111,
         87.03203,  101.04768,   99.06841,  186.07931,  163.06333])

a = np.fromfile('rosalind_sgra.txt', sep='\n')

spec = np.array(sorted(a))
n = len(spec)
G = nx.DiGraph()
G.add_nodes_from(range(n))

for i in range(n-1):
    for j in range(i+1, n):
        d = spec[i] - spec[j]
        if (abs(mass + d) < 0.0001).any():
            aa = residue[np.where(abs(mass + d) < 0.0001)[0][0]]
            G.add_edge(i, j, label=aa)

path = nx.dag_longest_path(G)
result = ''.join([G[u][v]['label'] for u, v in zip(path[:-1], path[1:])])

open('rosalind_sgra_sub.txt', 'wt').write(result)
print(result)