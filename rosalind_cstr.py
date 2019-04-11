#rosalind_cstr
'''
A collection of strings is characterizable if there are at most two possible 
choices for the symbol at each position of the strings.

Given: A collection of at most 100 characterizable DNA strings, 
each of length at most 300 bp.

Return: A character table for which each nontrivial character encodes 
the symbol choice at a single position of the strings. 
(Note: the choice of assigning '1' and '0' to the two states of each SNP in 
the strings is arbitrary.)
'''
import numpy as np

s = open('rosalind_cstr.txt').read().rstrip().split()
t = np.array([list(i) for i in s]).T

n = len(t[0])

cstr = []
for i in range(n):
    split = np.array(t[i] == t[i][0], int)
    if sum(split) not in (1, n-1):
        cstr.append(split)

result = '\n'.join([''.join([str(i) for i in row]) for row in cstr])
print(result)

open('rosalind_cstr_sub.txt', 'wt').write(result)
   
'''A trivial character isolates a single taxon into a group of its own. 
The corresponding split S∣Sc must be such that S or Sc contains only one element; 
the edge encoded by this split must be incident to a leaf of 
the unrooted binary tree, and the array for the character contains 
exactly one 0 or exactly one 1. Trivial characters are of no phylogenetic 
interest because they fail to provide us with information regarding the 
relationships of taxa to each other. All other characters are called 
nontrivial characters (and the associated splits are called nontrivial splits).

A character table is a matrix C in which each row represents the array notation 
for a nontrivial character. That is, entry Ci,j denotes the "ON"/"OFF" position 
of the i-th character with respect to the j-th taxon.
'''

