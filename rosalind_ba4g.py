#rosalind_ba4f
import numpy as np
from itertools import permutations
from collections import Counter

aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
          'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
          'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
aa_mw = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def cyclospectrum(peptide):
    '''peptide is weight list'''
    
    length = len(peptide)
    wheel = peptide + peptide
    
    ions = [wheel[i:i+j+1] for i in range(length) for j in range(length-1)]
    ions.append(peptide)
    return [0] + sorted([sum(p) for p in ions])

def score(peptide, spec):
    spec_counts = Counter(spec)
    ideal_counts = Counter(cyclospectrum(peptide))
    return sum([min(ideal_counts[k], spec_counts[k]) for k in spec_counts])

def expand(residues):
    for p in permutations(residues[1:]):
        yield residues[:1] + list(p)


f = open('rosalind_ba4g.txt')
N = int(f.readline().rstrip())

spec = np.fromfile(f, sep=' ', dtype=int)

leader_board = dict(((i,), 0) for i in spec if i in aa_mw)
leader_peptide = (0,)
while len(leader_board) != 0:
    leader_board = { p + (aa,): score(p + (aa,), spec)  
                     for p in leader_board for aa in aa_mw }
    for p, s in leader_board.items():
        if sum(p) == spec[-1]:
            if s > score(leader_peptide, spec):
                leader_peptide = p
    
    leader_board = {p: s for p, s in leader_board.items() if sum(p) <= spec[-1]}
     
    if len(leader_board) > N:
        cutoff_score = sorted(leader_board.values())[-N]
        leader_board = { p: s for p, s in leader_board.items() if s >= cutoff_score}        
            
print('-'.join([str(i) for i in leader_peptide]))
