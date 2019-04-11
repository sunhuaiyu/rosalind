#rosalind_med

import numpy as np

f = open('rosalind_med.txt')
n = int(f.readline().strip())
A = np.array([int(i) for i in f.readline().rstrip().split()])
k = int(f.readline().strip())


print(sorted(A)[k-1])