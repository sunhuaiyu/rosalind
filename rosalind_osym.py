#rosalind_osym
import numpy as np
from Bio import SeqIO

match_score = (-1, 1) # -1 penalty for mismatch; +1 award for match
gap_penalty = -1

def needleman_wunsch(seq1, seq2):
    '''Needleman-Wunsch Algorithm'''
    m, n = len(seq1), len(seq2) 
    score_table = np.zeros((m+1, n+1), int)    
   
    # Initialize Needleman-Wunsch score table
    score_table[:, 0] = np.arange(m + 1) * gap_penalty
    score_table[0, :] = np.arange(n + 1) * gap_penalty
        
    for i in range(m):
        for j in range(n):
            match = score_table[i, j] + match_score[seq1[i] == seq2[j]]
            delete = score_table[i, j+1] + gap_penalty
            insert = score_table[i+1, j] + gap_penalty
            score_table[i+1, j+1] = max(match, delete, insert)
    
    return score_table

s, t = [str(i.seq) for i in SeqIO.parse('rosalind_osym.txt', 'fasta')]
m, n = len(s), len(t)

# do Needleman-Wunsch in both forward and reversed directions
needle = needleman_wunsch(s, t)
needle2 = needleman_wunsch(s[::-1], t[::-1])

mat = np.zeros((m, n), int)
for i in range(m):
    for j in range(n):
        mat[i, j] =  needle[i, j] + match_score[s[i]==t[j]] + needle2[m-i-1, n-j-1]
print(needle[-1, -1], mat.sum(), sep='\n')
