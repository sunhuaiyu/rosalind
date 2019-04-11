# rosalind_ba8c

import numpy as np
from scipy.cluster.vq import kmeans2

f = open('rosalind_ba8c.txt')
k, m = [int(i) for i in f.readline().rstrip().split()]

data = np.fromfile(f, sep=' ').reshape(-1, m)

centers = np.round(kmeans2(data, data[:k], iter=50)[0], 3)
result = '\n'.join([' '.join([str(i) for i in row]) for row in centers])

print(result)
open('rosalind_ba8c_sub.txt', 'wt').write(result)