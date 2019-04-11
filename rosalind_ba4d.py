# rosalind_ba4d
import numpy as np
import networkx as nx

def count_path(m):
    '''Compute the number of peptides of given total mass, assuming no
    difference between K/Q or I/L. The N-th power of the adjacency matrix 
    contains the count of length-N path from 0 to m at entry [0, m].'''
    
    aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
          'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
          'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

    G = nx.DiGraph()
    for i in range(0, m):
        for j in range(1, m+1):
            if j - i in aa_mass.values():
                G.add_edge(i, j)

    mat = nx.to_scipy_sparse_matrix(G)   #default nodelist

    longest = m // aa_mass['G']
    shortest = m // aa_mass['W'] + 1
    return sum([(mat **i)[0, m] for i in range(shortest, longest+1)])

mass = int(open('rosalind_ba4d.txt').readline().rstrip())
  
print(count_path(mass))


################## other's much faster, more elegant
def CountingPeptidesWithGivenMass(mass):
    aminoAcidMasses = [57,71,87,97,99,101,103,113,114,
                       115,128,129,131,137,147,156,163,186] #unique ones
    linearPeptideMap = { 0: 1 }
    for i in range(57, mass+1):
        for aaMass in aminoAcidMasses:
            linearPeptideMap[i] = ( linearPeptideMap.get(i - aaMass, 0) 
                                    + linearPeptideMap.get(i, 0) )
    return linearPeptideMap[mass]



