# rosalind_ba1d
# k-mer 

import numpy as np

kmer, seq = [i.rstrip() for i in open('rosalind_ba1d.txt')]
k = len(kmer)
s = len(seq)

out = np.array([i for i in range(s - k + 1) if seq[i:i+k] == kmer])
out.tofile('rosalind_ba1d_sub.txt', sep=' ')

