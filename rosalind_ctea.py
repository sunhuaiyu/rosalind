# rosalind_ctea
import numpy as np
from Bio import SeqIO

#Based on Needleman-Wunsch Algorithm; Scoring for Edit Distance
def ctea(seq1, seq2):
    P = 134217727  # P = 2**27 -1
    
    #(match, mismatch, gap_penalty) == (0, -1, -1) <=> a negative edit_distance
    match_score = (-1, 0) # -1 penalty for mismatch; no award for match
    gap_penalty = -1

    m, n = len(seq1), len(seq2) 
    
    score_table = np.zeros((m+1, n+1), int)    
    count_table = np.zeros((m+1, n+1), int)
   
    # Initialize Needleman-Wunsch score table
    score_table[:, 0] = np.arange(m + 1) * gap_penalty
    score_table[0, :] = np.arange(n + 1) * gap_penalty
    
    # Initialize count table
    count_table[:, 0] = 1
    count_table[0, :] = 1
    
    for i in range(m):
        for j in range(n):
            match = score_table[i, j] + match_score[seq1[i] == seq2[j]]
            delete = score_table[i, j+1] + gap_penalty
            insert = score_table[i+1, j] + gap_penalty
            score_table[i+1, j+1] = max(match, delete, insert)
            
            # summation of "in-coming edges" in the score_table
            if score_table[i+1, j+1] == match:
                count_table[i+1, j+1] += count_table[i, j] % P
            if score_table[i+1, j+1] == delete:
                count_table[i+1, j+1] += count_table[i, j+1] % P
            if score_table[i+1, j+1] == insert:
                count_table[i+1, j+1] += count_table[i+1, j] % P
    
    #return score_table[m, n] # negative edit distance
    return count_table[m, n]

s, t = [str(i.seq) for i in SeqIO.parse('rosalind_ctea.txt', 'fasta')]
print(ctea(s, t))

