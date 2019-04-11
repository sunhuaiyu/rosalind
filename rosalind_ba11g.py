#rosalind_ba11g
'''
PSM Search Problem:
Identify Peptide-Spectrum Matches by matching spectra against a proteome.

Given: A set of space-delimited spectral vectors SpectralVectors, 
an amino acid string Proteome, and a score threshold T.

Return: All unique Peptide-Spectrum Matches scoring at least as high as T.

PSMSearch(SpectralVectors, Proteome, threshold).
    PSMSet ← an empty set
    for each vector Spectrum' in SpectralVectors
          Peptide ← PeptideIdentification(Spectrum', Proteome)
          if Score(Peptide, Spectrum) ≥ threshold
              add the PSM (Peptide, Spectrum') to PSMSet
    return PSMSet

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


def peptide_identification(proteome, spec):
    '''identify a peptide in proteome with highest score against the spec vector'''
    m = len(spec) -1 # size of original spec vector == weight of target peptides
    max_score = 0
    id_result = ''
    for p in mass_filter(proteome, m):
        peptide = proteome[p[0]:p[1]]
        vector = np.array([0] + [aa_mass[i] for i in peptide]).cumsum()
        score = sum([spec[i] for i in vector]) #peptide weight given by spec
        if score > max_score:
            max_score = score
            id_result = peptide
    return [max_score, id_result]


def PSMsearch(spec_vectors, proteome, threshold): 
    PSMset = set()
    for s in spec_vectors:
        score, peptide = peptide_identification(proteome, s)
        if score >= threshold:
            PSMset.add(peptide)
    return PSMset


f = open('rosalind_ba11g.txt')

specs = []     # collection of all spectrum vectors

line = f.readline().rstrip()
while line[0] not in 'ACEDGFIHKMLNQPSRTWVY':
    # 0 inserted at the beginning of the spec vector
    specs.append(np.array(['0'] + line.split(), dtype=int)) 
    line = f.readline().rstrip()
proteome = line
T = int(f.readline().rstrip()) #scoring threshold

result = '\n'.join(PSMsearch(specs, proteome, T))
print(result)
