# sun.huaiyu
# 2d

import numpy as np
from itertools import combinations_with_replacement

aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
 'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

aa = list('GASPVTCILNDKQEMHFRYW')
mass = np.array([57, 71, 87, 97, 99, 101, 103, 113, 113, 114, 115, 128, 
                 128, 129, 131, 137, 147, 156, 163, 186])

#m = int(open('rosalind_2d.txt').readline().rstrip())
m = 1024

n_max = int(m / aa_mass['G'])
n_min = int(m / aa_mass['W'])

n_peptides = 0
peptides = []
for i in range(n_min, n_max + 1, 1):
    for p in combinations_with_replacement(aa, i):
        if sum([aa_mass[k] for k in p]) == m:
            peptides.append(p)

print(n_peptides)

