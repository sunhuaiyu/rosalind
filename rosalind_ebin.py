# rosalind_ebin


import numpy as np
from scipy.stats import binom

n, p = [line.rstrip() for line in open('rosalind_ebin.txt').readlines()]
n = int(n)
p = np.array(p.split()).astype(float)

out = n * p
out.tofile('rosalind_ebin_sub.txt', sep=' ')

