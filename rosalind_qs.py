#rosalind_qs

import numpy as np

f = open('rosalind_qs.txt')
n = int(f.readline().strip())
A = np.fromfile(f, sep=' ', dtype=int)

A.sort()
A.tofile('rosalind_qs_sub.txt', sep=' ')