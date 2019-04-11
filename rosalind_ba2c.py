#rosalind_ba2c
'''
Profile-most probable k-mer in a string.

Given: A string Text, an integer k, and a 4 × k matrix Profile.
Return: A Profile-most probable k-mer in Text. 
(If multiple answers exist, you may return any one.)
'''

import numpy as np

def all_kmers(seq, k): # to find the k-mer composition of a string
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def kmer2matrix(kmer):
    d = {'A':[1, 0, 0, 0], 'C':[0, 1, 0, 0], 'G':[0, 0, 1, 0], 'T':[0, 0, 0, 1]}
    return np.array([d[i] for i in kmer]).T

def profile(seq_array, k):
    '''
    Given an array of k-mers, each with length k, return the nucleotide counts 
    at each position (0 ~ k-1) as a 4 x k array, in the order of 'ACGT'. 
    '''
    m = [[[s[i] for s in seq_array].count(a) for i in range(k)] for a in 'ACGT']
    m = np.array(m) 
    return m

def profile_most_probable_kmer(seq, k, p):
    '''
    Given a string seq and a k-mer profile p (a 4 x k array,
    with each column the fractions of ACGT counts at each position 0 ~ k-1), 
    return a k-mer in seq that best matches the profile.
    '''
    kmers = all_kmers(seq, k)
    counts = np.array([profile([i], k) for i in kmers])
    scores = np.product((p * counts).sum(1), axis=1)
    return kmers[scores.argmax()]

# read data
f = open('rosalind_ba2c.txt').readlines()
seq = f[0].rstrip()
k = int(f[1].rstrip())
m = np.array([i.rstrip().split() for i in f[2:]]).astype(float)

print(profile_most_probable_kmer(seq, k, m))
