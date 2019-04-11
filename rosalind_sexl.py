# rosalind_sexl

import numpy as np

A = np.array([i for i in open('rosalind_sexl.txt').readline().rstrip().split()]).astype(float)

(1 - (1-A)**2 - A**2).tofile('rosalind_sexl_sub.txt', sep=' ')
