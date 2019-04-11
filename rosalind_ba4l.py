#rosalind_ba4k
import numpy as np
from collections import Counter

def linearspectrum(peptide):
    aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
     'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
    'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
    n = len(peptide)
    prefix_mass = np.array([0] + [aa_mass[i] for i in peptide]).cumsum()
    
    lin_spec = [0]
    for i in range(n):
        for j in range(i+1, n+1):
            lin_spec.append(prefix_mass[j] - prefix_mass[i])  
    return sorted(lin_spec)

def score(peptide, spec):
    '''peptide as amino acid string'''
    spec_counts = Counter(spec)
    ideal_counts = Counter(linearspectrum(peptide))
    return sum([min(ideal_counts[k], spec_counts[k]) for k in spec_counts])

def trim(leader_board, spec, N):
    score_board = {peptide: score(peptide, spec) for peptide in leader_board}
    if len(leader_board) > N:
        cutoff_score = sorted(score_board.values())[-N]
        leader_board = [p for p in score_board if score_board[p] >= cutoff_score]
    return leader_board


f = open('rosalind_ba4l.txt')
leader_board = f.readline().rstrip().split()
spec = np.array(f.readline().rstrip().split(), dtype=int)
N = int(f.readline().rstrip())

result = ' '.join(trim(leader_board, spec, N))
open('rosalind_ba4l_sub.txt', 'wt').write(result)
