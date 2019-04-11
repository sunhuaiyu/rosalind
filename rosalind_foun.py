# rosalind_foun

import numpy as np
from scipy.stats import binom


file = open('rosalind_foun.txt')
N, m = [int(i) for i in file.readline().rstrip().split()]
A = np.array([int(i) for i in file.readline().rstrip().split()])

def drift(n, m, g):
    p = m / (2.0 * n)
    p_arr = binom(2*n, p).pmf(arange(2*n + 1))

    for j in range(1, g):
        B = np.zeros((2*n + 1,), dtype=float)
        for i in arange(2*n + 1):
            B += p_arr[i] * binom(2*n, i/(2*n)).pmf(arange(2*n + 1))            
        p_arr = B 
    return np.log10(p_arr[0])

out = np.array([[drift(N, j, i) for j in A] for i in range(1, m + 1)])
out.tofile('rosalind_foun_sub.txt', sep=' ')
