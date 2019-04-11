# rosalind_bins

import numpy as np
f = open('rosalind_bins.txt')

n = int(f.readline().rstrip())
m = int(f.readline().rstrip())
A = [int(i) for i in f.readline().rstrip().split()]
k = [int(i) for i in f.readline().rstrip().split()]

d = dict(zip(A, np.arange(n)+1))
result = [d.get(i, -1) for i in k]
print(result)
open('rosalind_bins_sub.txt', 'wt').write(' '.join([str(i) for i in result]))
