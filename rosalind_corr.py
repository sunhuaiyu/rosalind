# rosalind_corr
# error correction in sequence reads

import numpy as np
from scipy.sparse.csgraph import connected_components

def revc(sequence):
    pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([pairs[i] for i in sequence][::-1])

def revc2(sequence):
    return sequence.translate({65: 84, 67: 71, 71: 67, 84: 65})[::-1]

def hamming(seq1, seq2):
    # assert len(seq1) == len(seq2), 'unequal reads!'
    return sum([i[0] != i[1] for i in zip(seq1, seq2)])

reads = []
for line in open('rosalind_corr.txt'):
    if line[0] != '>':
        reads.append(line.rstrip())
n = len(reads)

# establish a hamming distance matrix
dist_matrix = np.zeros((n, n), dtype=int)
for i in range(n):
    for j in range(i+1, n):
        ham_dist = min(hamming(reads[i], reads[j]), hamming(reads[i], revc(reads[j])))
        dist_matrix[i, j] = ham_dist
dist_matrix = dist_matrix + dist_matrix.T

# establish a graph with identical reads as connected nodes, 
# get the labels of connected components
connected = connected_components((dist_matrix==0).astype(int), directed=False)[1] 

# indices of "un-connected" reads -- the row from dist_matrix should have --
# (1) only 1 zero (not a correct read)
# (2) >= 2 entries with hamming == 1, indicative of a single mismatched correct read
# and (3), implemented later,
# the entries with hamming == 1 must point to only 1 correct read

incorrect = np.where(((dist_matrix == 0).sum(1) == 1) & 
                     ((dist_matrix == 1).sum(1) >= 2))[0]

f = open('rosalind_corr_sub.txt', 'wt')
for i in incorrect:
    single_mismatches = np.where(dist_matrix[i] == 1)[0]
    labels, index, counts = np.unique(connected[single_mismatches], 
                                      return_index=True, return_counts=True)
    index = index[counts >= 2]
            
    # the labels should contain only 1 connected components for a unique correct read set
    if len(index) == 1:        
        seq = reads[single_mismatches[index[0]]]
        if hamming(reads[i], seq) != 1: 
            seq = revc(seq)
        f.write(reads[i] + '->' + seq + '\n')
f.close()


