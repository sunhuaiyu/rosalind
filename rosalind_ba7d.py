# rosalind_ba7d
'''
Construct the ultrametric tree resulting from UPGMA.

Given: An integer n followed by a space-delimited n x n distance matrix.

Return: An adjacency list for the ultrametric tree output by UPGMA. Weights 
should be accurate to three decimal places.

Note on formatting: The adjacency list must have consecutive integer node labels 
starting from 0. The n leaves must be labeled 0, 1, ..., n-1 in order of their 
appearance in the distance matrix. Labels for internal nodes may be labeled in 
any order but must start from n and increase consecutively.

ultrametricize: Sets all root-to-tip path lengths equal by stretching
all terminal branches to the height of the tallest node.
'''

import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import squareform

f = open('rosalind_ba7d.txt')
n = int(f.readline().rstrip())

D = np.fromfile(f, sep=' ', dtype=int).reshape(n, n)

d = squareform(D)
m = linkage(squareform(D), method='average')

result = []
age = {i: 0 for i in range(n)}
for i in range(n-1):
    age[n+i] = round(m[i, 2] / 2, 3)
    u, v = m[i, :2].astype(int)
    w = age[n+i] - age[u]
    result.append([str(u), str(n+i), str(w)])
    result.append([str(n+i), str(u), str(w)])
    w = age[n+i] - age[v]
    result.append([str(v), str(n+i), str(w)])
    result.append([str(n+i), str(v), str(w)])


result = sorted(result, key=lambda x: int(x[0]))
result = [i[0] + '->' + i[1] + ':' + i[2] for i in result]
open('rosalind_ba7d_sub.txt', 'wt').write('\n'.join(result))
