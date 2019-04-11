# rosalind_ba11c
'''
Given an amino acid string Peptide = a1 . . . an of length n, we will represent 
its prefix masses using a binary peptide vector Peptide' with mass(Peptide) coordinates. 
This vector contains a 1 at each of the n prefix coordinates
        mass(a1), mass(a1 a2), . . . , mass(a1 a2 . . . an ) ,
and it contains a 0 in each of the remaining noise coordinates. The toy peptide XZZXX, 
whose prefix masses are 4, 9, 14, 18, and 22, corresponds to the peptide vector 
(0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1) of length 22.

Converting Peptide into Peptide Vector Problem: 
Convert a peptide into a binary peptide vector.

Given: A peptide P.
Return: The peptide vector of P.
'''

import numpy as np

aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
 'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163, 'X': 4, 'Z': 5}

    
peptide = open('rosalind_ba11c.txt').readline().rstrip()
total_mass = sum([aa_mass[k] for k in peptide])

vector = np.zeros(total_mass, dtype=int)
vector[total_mass-1] = 1

prefix = [peptide[:k] for k in range(1, len(peptide))] 
prefix_spec = np.array([sum([aa_mass[k] for k in p]) for p in prefix])

vector[prefix_spec-1] = 1

vector.tofile('rosalind_ba11c_sub.txt', sep=' ')




