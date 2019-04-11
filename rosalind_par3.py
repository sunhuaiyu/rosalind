#rosalind_par

import numpy as np

f = open('rosalind_par3.txt')
n = int(f.readline().strip())

A = np.fromfile(f, sep=' ', dtype=int)

B = np.concatenate((A[A < A[0]], A[A == A[0]], A[A > A[0]]))

B.tofile('rosalind_par3_sub.txt', sep=' ')