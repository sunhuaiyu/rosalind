#rosalind_ba4e
import numpy as np
from itertools import permutations

aa_mw = [57,71,87,97,99,101,103,113,114,115,128,129,131,137,147,156,163,186]

def cyclospectrum(peptide):
    '''peptide is a list of aa_mw values'''
    length = len(peptide)
    wheel = peptide + peptide
    
    ions = [wheel[i:i+j+1] for i in range(length) for j in range(length-1)]
    return sorted([sum(p) for p in ions])


def cyclopeptidesequence(spectrum, residues):
    '''spectrum is a numpy array'''
    out = set()
    peptides = [residues[:1] + list(p) for p in permutations(residues[1:])]
    while peptides != []:
        peptide = peptides.pop()
        if cyclospectrum(peptide) == list(spectrum[1:-1]):
            out.add(tuple(peptide))
    return out

spectrum = np.fromfile('rosalind_ba4e.txt', sep=' ', dtype=int)

# find the amino acid composition
residues = []
for i in spectrum[1:]:
    residues.append(i)
    if sum(residues) == spectrum[-1]:
        break

cyclo = cyclopeptidesequence(spectrum, residues)
result = set([p[i:] + p[:i] for p in cyclo for i in range(len(residues))])

result = ' '.join(['-'.join([str(i) for i in p]) for p in result])
open('rosalind_ba4e_sub.txt', 'wt').write(result)

