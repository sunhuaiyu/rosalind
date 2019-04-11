#rosalind_par

import numpy as np

f = open('rosalind_par.txt')
n = int(f.readline().strip())

A = np.fromfile(f, sep=' ', dtype=int)
A1 = A[1:]

B = np.concatenate((A1[A1 <= A[0]], A[0:1], A1[A1 > A[0]]))

B.tofile('rosalind_par_sub.txt', sep=' ')