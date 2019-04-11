# rosalind_ba8e

import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import squareform

f = open('rosalind_ba8e.txt')
n = int(f.readline().rstrip())

D = np.fromfile(f, sep=' ', dtype=float).reshape(n, n)

m = linkage(squareform(D), method='average')

clusters = {i:[i] for i in range(n)}
for i in range(n-1):
    u, v = m[i, :2].astype(int)
    clusters[n+i] = clusters[u] + clusters[v]

result = []
i = n
while i in clusters:
    result.append(' '.join([str(j+1) for j in clusters[i]]))
    i += 1
    
open('rosalind_ba8e_sub.txt', 'wt').write('\n'.join(result))
