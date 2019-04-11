# Huaiyu Sun
# CONS
from Bio import SeqIO
import numpy as np

def profile(seq_array):
    k = len(seq_array[0])
    '''
    Given an array of k-mers, each with length k, return the nucleotide counts 
    at each position (0 ~ k-1) as a 4 x k array, in the order of 'ACGT'. 
    '''
    m = [[[s[i] for s in seq_array].count(a) for i in range(k)] for a in 'ACGT']
    m = np.array(m) 
    return m


seq = [str(i.seq) for i in SeqIO.parse('rosalind_cons.txt', 'fasta')]

profile_matrix = profile(seq)

nt = np.array(['A', 'C', 'G', 'T'])
consensus = ''.join([nt[i == i.max()][0] for i in profile_matrix.T ])

result = [consensus] + [nt[i] + ': ' + ' '.join([str(j) for j in profile_matrix[i]]) 
                         for i in range(4)]

open('rosalind_cons_ans.txt', 'wt').write('\n'.join(result))

