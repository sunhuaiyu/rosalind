# rosalind_wfmd
'''
Given: Positive integers N (N≤7), m (m≤2N), g(g≤6) and k (k≤2N).
Return: The probability that in a population of N diploid individuals 
initially possessing m copies of a dominant allele, we will observe 
after g generations at least k copies of a recessive allele. 
Assume the Wright-Fisher model.
'''

import numpy as np
from scipy.stats import binom

n, m, g, k = np.array(open('rosalind_wfmd.txt').readline().rstrip().split()).astype(int)

p = 1 - m / (2.0 * n)
p_arr = binom(2*n, p).pmf(arange(2*n + 1))

for j in range(1, g):
    B = np.zeros((2*n + 1,), dtype=float)
    for i in arange(2*n + 1):
        B += p_arr[i] * binom(2*n, i/(2*n)).pmf(arange(2*n + 1))            
    p_arr = B 
          
out = p_arr[k:].sum()
print(out)


