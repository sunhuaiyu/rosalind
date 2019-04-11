'''A   71.03711
C   103.00919
D   115.02694
E   129.04259
F   147.06841
G   57.02146
H   137.05891
I   113.08406
K   128.09496
L   113.08406
M   131.04049
N   114.04293
P   97.05276
Q   128.05858
R   156.10111
S   87.03203
T   101.04768
V   99.06841
W   186.07931
Y   163.06333'''

import pandas as pd; from pandas import DataFrame, Series

import numpy as np
t = [i.rstrip().split() for i in open('monoisotopic_mass_table.txt').readlines()]
mass = DataFrame(t, columns=['residue', 'mass'], dtype=float)

residue = np.array(mass.residue)
mass = np.array(mass.mass)

spec = Series(open('rosalind_spec.txt').readlines(), dtype=float)
increment = np.array(spec.diff()[1:])

peptide = ''.join([residue[np.where(abs(mass - i) < 0.0001)[0][0]] for i in increment])

f = open('rosalind_spec_sub.txt', 'wt')
f.write(peptide)
f.close()
