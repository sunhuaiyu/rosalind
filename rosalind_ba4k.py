#rosalind_ba4k
import numpy as np

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


f = open('rosalind_ba4k.txt')
seq = f.readline().rstrip()
spec = np.fromfile(f, sep=' ', dtype=int)

ideal = np.array(linearspectrum(seq))

spec_dict = dict(zip(*np.unique(spec, return_counts=1)))
ideal_dict = dict(zip(*np.unique(ideal, return_counts=1)))

score = 0
for k in spec_dict:
    score += min(spec_dict.get(k, 0), ideal_dict.get(k, 0))

print(score)
