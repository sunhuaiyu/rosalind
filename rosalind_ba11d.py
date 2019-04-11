#rosalind_ba11d

import numpy as np

mass_aa = {71: 'A', 103: 'C', 129: 'E', 115: 'D', 57: 'G', 147: 'F', 
 113: 'I', 137: 'H', 128: 'K', 131: 'M', 114: 'N', 97: 'P', 87: 'S', 
 156: 'R', 101: 'T', 186: 'W', 99: 'V', 163: 'Y', 4: 'X', 5: 'Z'}

vector = np.fromfile('rosalind_ba11d.txt', sep=' ', dtype=int)

spec = np.where(vector == 1)[0]

peptide = mass_aa[spec[0]+1]
for i in np.diff(spec):
    peptide += mass_aa[i]

print(peptide)
open('rosalind_ba11d_sub.txt', 'wt').write(peptide)
