#rosalind_ba11f
'''
Peptide Identification Problem:
Find a peptide from a proteome with maximum score against a spectrum.

Given: A space-delimited spectral vector S and an amino acid string Proteome.

Return: A peptide in proteome with maximum score against S.
'''
import numpy as np
import networkx as nx

aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
     'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
     'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163} #'X': 4, 'Z': 5}

def mass_filter(seq, mass):
    '''Sliding-window through the proteome (seq), vary window width according to 
    the difference between the resulting peptide mass (w) and the given mass (mass); 
    find all substrings of seq with weight == mass, return range indices.'''
        
    n = len(seq)
    i, j = 0, 1
    w = aa_mass[seq[i]]    # weight of peptide
    collection = []
    while j < n:
        if w == mass:
            collection.append((i, j))
            w -= aa_mass[seq[i]]
            i += 1
            w += aa_mass[seq[j]]
            j += 1
        elif w > mass:
            w -= aa_mass[seq[i]]
            i += 1
        else:
            w += aa_mass[seq[j]]
            j += 1
    return collection


f = open('rosalind_ba11f.txt')
spec = np.array(['0'] + f.readline().rstrip().split(), dtype=int)
proteome = f.readline().rstrip()

m = len(spec) - 1 # size of the original spec vector
max_score = 0
result = ''
for p in mass_filter(proteome, m):
    peptide = proteome[p[0]:p[1]]
    vector = np.array([0] + [aa_mass[i] for i in peptide]).cumsum()
    
    '''The same score can be computed otherwise as the dot product of 
    the spectrum vector and the binary peptide vector.'''
    score = sum([spec[i] for i in vector])
    
    if score > max_score:
        max_score = score
        result = peptide

print(result)
