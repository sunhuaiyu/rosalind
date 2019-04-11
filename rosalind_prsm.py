#rosalind_prsm

import numpy as np
from itertools import product

def peptide_mass(peptide):

    residue_MW_table = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496,
        'L': 113.08406, 'M': 131.04049,'N': 114.04293, 'P': 97.05276,  'Q': 128.05858,
        'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841,  'W': 186.07931,
        'Y': 163.06333}

    return sum([residue_MW_table[i] for i in peptide])

def largest_multiplicity(x, y):
    d = np.array([abs(i[0] - i[1]) for i in product(x, y)])
    d = np.sort(d)

    dd = np.diff(d) < 0.000001
    dd = dd.astype(int)
    
    # find the longest run of 1s in dd
    run_longest = 0
    run_length = 0
    pos = 0
    i, l = 0, len(dd)
    while i < l:
        run_length = 0
        while i < l and dd[i] == 1:
            run_length += 1
            i += 1
        if run_length > run_longest:
            run_longest = run_length
            pos = i
        i += 1

    return (run_longest+1, d[pos])        

f = open('rosalind_prsm.txt').readlines()
n = int(f[0].rstrip())
proteins = [s.rstrip() for s in f[1:n+1]]
spec = np.array([s.rstrip() for s in f[n+1:]]).astype(float)

multiplicity = []
for p in proteins:
    prefix = [p[:i] for i in range(1, len(p))]
    suffix = [p[i:] for i in range(len(p))]
    all_pep = set(prefix) | set(suffix)
    all_mass = [peptide_mass(i) for i in all_pep]
    multiplicity.append([largest_multiplicity(all_mass, spec)[0], p])

out = max(multiplicity, key=lambda x: x[0])
open('rosalind_prsm_sub.txt', 'wt').write(str(out[0]) + '\n' + out[1])

