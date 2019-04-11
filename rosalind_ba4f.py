#rosalind_ba4f
import numpy as np

def cyclospectrum(peptide):
    '''peptide is sequence'''
    
    aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
          'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
          'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
    length = len(peptide)
    wheel = peptide + peptide
    
    ions = [wheel[i:i+j+1] for i in range(length) for j in range(length-1)]
    ions.append(peptide)
    return [0] + sorted([sum(list(map(lambda x: aa_mass[x], p))) for p in ions])

f = open('rosalind_ba4f.txt')
seq = f.readline().rstrip()
spec = np.fromfile(f, sep=' ', dtype=int)

ideal = np.array(cyclospectrum(seq))

spec_dict = dict(zip(*np.unique(spec, return_counts=1)))
ideal_dict = dict(zip(*np.unique(ideal, return_counts=1)))

score = 0
for k in spec_dict:
    score += min(spec_dict.get(k, 0), ideal_dict.get(k, 0))

print(score)
