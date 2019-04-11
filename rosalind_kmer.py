# rosalind_kmer
# k-mer composition

from itertools import product
import numpy as np
k = 4

lex = array([''.join(i) for i in product('ACGT', repeat=4)])

seq = ''.join([line.rstrip() for line in open('rosalind_kmer.txt').readlines()[1:]])
all_kmers = [seq[i:i+k] for i in range(len(seq) - k + 1)]

unique_kmers, counts = np.unique(all_kmers, return_counts=1)

out = np.array([dict(zip(unique_kmers, counts)).get(i, 0) for i in lex])

out.tofile('rosalind_kmer_sub.txt', sep=' ')

