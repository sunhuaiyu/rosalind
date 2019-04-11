# rosalind_ba2h
import numpy as np

def all_kmers(seq, k): 
	'''return the k-mer composition of a string'''
	return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def kmer2matrix(kmer):
	'''
	Covert a single k-mer to a (4, k) matrix in the order of 'ACGT'.
	'''
	d = {'A':[1, 0, 0, 0], 'C':[0, 1, 0, 0], 'G':[0, 0, 1, 0], 'T':[0, 0, 0, 1]}
	return np.array([d[i] for i in kmer]).T


def DistanceBetweenPatternAndStrings(Pattern, Dna):
    k = len(Pattern)
    d = 0
    for text in Dna:
        hamming = np.inf
        for i in all_kmers(text, k):
            hamming = min(hamming, k - (kmer2matrix(Pattern) * kmer2matrix(i)).sum())
        d += hamming
    return d
    

f = open('rosalind_ba2h.txt')
kmer = f.readline().rstrip()
dna = f.read().split()

print(DistanceBetweenPatternAndStrings(kmer, dna))

