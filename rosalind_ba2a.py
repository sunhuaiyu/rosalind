#rosalind_ba2a
'''
Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif
if it appears in every string from Dna with at most d mismatches.

Given: Integers k and d, followed by a collection of strings Dna.
Return: All (k, d)-motifs in Dna.
'''
from itertools import combinations, product
import numpy as np

def d_neighbors(p, d):  # to generate the d neighborhood of string p 
    #d-mers to replace 
    replacements = np.array(list(product('ACGT', repeat=d)))
    #positions (d points each) for mutation
    positions = np.array(list(combinations(range(len(p)), d)))

    out = set()
    for i in positions:
        t = np.array(list(p))
        for j in replacements:
            t[i] = list(j)
            out.add(''.join(t))
    return out 

def all_kmers(seq, k): # to find all k-mers of a string
    return set([seq[i:i+k] for i in range(len(seq) - k + 1)])

def motif_enumeration(Dna, k, d):
    Patterns = set()    
    for kmer in all_kmers(Dna, k):
        for i in d_neighbors(kmer, d):
            Patterns.add(i)
    return Patterns
    
f = open('rosalind_ba2a.txt').readlines()
k, d = [int(i) for i in f[0].rstrip().split()]
all_Dna = [i.rstrip() for i in f[1:]]

all_patterns = [motif_enumeration(Dna, k, d) for Dna in all_Dna]

result = set.intersection(*all_patterns)
open('rosalind_ba2a_sub.txt', 'wt').write(' '.join(result))


