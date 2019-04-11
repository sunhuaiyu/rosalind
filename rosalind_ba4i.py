#rosalind_ba4i

import numpy as np
from collections import Counter

def conv(spectrum, M):
    '''top M elements (and ties) between 57 and 200 from the convolution of Spectrum'''
    spec = [0] + list(spectrum)
    convolution = [j-i for j in spec[1:] for i in spec[:-1] if j > i]

    counts = Counter([i for i in convolution if i>=57 and i<=200])

    result = []
    # sort convolution d by value_counts, return the top M values in d 
    for k in sorted(counts, key=lambda x: counts[x], reverse=True)[:M]:
        result += [k] * counts[k]
    return result


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

# aa_mw = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]
def leader_board_sequencing(spec, N, aa_set):
    leader_board = dict(((i,), 0) for i in spec if i in aa_set)
    leader_peptide = (0,)
    while len(leader_board) != 0:
        leader_board = { p + (aa,): score(p + (aa,), spec)  
                         for p in leader_board for aa in aa_set }
        for p, s in leader_board.items():
            if sum(p) == spec[-1]:
                if s > score(leader_peptide, spec):
                    leader_peptide = p
    
        leader_board = {p: s for p, s in leader_board.items() if sum(p) <= spec[-1]}
     
        if len(leader_board) > N:
            cutoff_score = sorted(leader_board.values())[-N]
            leader_board = { p: s for p, s in leader_board.items() if s >= cutoff_score}        
    return leader_peptide

f = open('rosalind_ba4i.txt')
M = int(f.readline().rstrip())
N = int(f.readline().rstrip())
spec = sorted(np.fromfile(f, sep=' ', dtype=int))

selected_mw = set(conv(spec, M))

leader_peptide = leader_board_sequencing(spec, N, selected_mw)
result = '-'.join([str(i) for i in leader_peptide])
print(result)
