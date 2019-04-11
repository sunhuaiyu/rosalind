# rosalind_ba2d
import numpy as np

def all_kmers(seq, k): # to find the k-mer composition of a string
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def profile(seq_array, k):
    '''
    Given an array of k-mers, each with length k, return the nucleotide profile 
    at each position (0 ~ k-1) as a 4 x k array, in the order of 'ACGT'. 
    '''
    m = [[[s[i] for s in seq_array].count(a) for i in range(k)] for a in 'ACGT']
    m = np.array(m) / len(seq_array) 
    return m

def profile_most_probable_kmer(seq, k, p):
    '''
    Given a string seq and a k-mer profile p (a 4 x k array,
    with each column the fractions of ACGT counts at each position 0 ~ k-1), 
    return a k-mer in seq that is most probably according to the profile.
    '''
    best_kmer = [0, '']
    score = 0
    kmers = all_kmers(seq, k)
    counts = np.array([profile([i], k) for i in kmers])
    scores = np.product((p * counts).sum(1), axis=1)   # the probability of each k-mer
    return kmers[scores.argmax()]

def greedy_motifsearch(dna, k, t):
    best_motifs = [i[:k] for i in dna]
    
    for kmer in all_kmers(dna[0], k):
        motifs = [kmer]
        
        for i in range(1, t):
            p_motifs = profile(motifs, k)       
            motifs.append(profile_most_probable_kmer(dna[i], k, p_motifs))
            p_best = profile(best_motifs, k)

        if (p_motifs * t).max(0).sum() > (p_best * t).max(0).sum():
            best_motifs = motifs.copy()
    return best_motifs

f = open('rosalind_ba2d.txt').readlines()
k, t = [int(i) for i in f[0].rstrip().split()]
dna = [i.strip() for i in f[1:]]

result = greedy_motifsearch(dna, k, t)
print('\n'.join(result))
open('rosalind_ba2d_sub.txt', 'wt').write('\n'.join(result))

