#rosalind_ba2b
'''
Median String Problem
Given: An integer k and a collection of strings Dna.
Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. 
(If multiple answers exist, you may return any one.)
'''
from itertools import combinations, product
import numpy as np

def all_kmers(seq, k): # to find the k-mer composition of a string
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def hamming(s, t):
    n = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            n += 1
    return n

f = open('rosalind_ba2b.txt').readlines()
k = int(f[0].rstrip())
dna = [i.rstrip() for i in f[1:]]

candidates = [''.join(i) for i in product('ACGT', repeat=k)]

d = ['', 1000000]
s = 0
for i in candidates:
    s = sum([min([hamming(i, j) for j in all_kmers(s, k)]) for s in dna])
    if s < d[1]:
        d[0] = i
        d[1] = s

print(d)


        




