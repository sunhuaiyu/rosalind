# rosalind_ba1f
# skew 

import numpy as np

s = open('rosalind_ba1f.txt').readline().rstrip()

n = len(s)

skew = np.zeros((n,), dtype=int)

d = {'G': 0, 'C':0}
for i in range(n):              
    if s[i] == 'G':
        d['G'] += 1
    elif s[i] == 'C':
        d['C'] += 1
    skew[i] = d['G'] - d['C']

out = np.where(skew == skew.min())[0] + 1

out.tofile('rosalind_ba1f_sub.txt', sep=' ')

