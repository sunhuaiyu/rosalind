# rosalind_ba2e
import numpy as np

def all_kmers(seq, k): # to find the k-mer composition of a string
    return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def count_matrix(seq_array, k):
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
    return a k-mer in seq that is most probably according to the profile.
    '''
    best_kmer = [0, '']
    score = 0
    kmers = all_kmers(seq, k)
    kmer_matrix = np.array([count_matrix([i], k) for i in kmers])
    
    #the probability of each k-mer given the profile p
    scores = np.product((p * kmer_matrix).sum(1), axis=1) 
      
    return kmers[scores.argmax()]


def greedy_motifsearch_pseudocounts(dna, k, t):
    best_motifs = [i[:k] for i in dna]
    
    for kmer in all_kmers(dna[0], k):
        motifs = [kmer]
        
        for i in range(1, t):
            profile = (count_matrix(motifs, k) + 1) / (len(motifs) + 4)     
            motifs.append(profile_most_probable_kmer(dna[i], k, profile))
             
            p_motifs = count_matrix(motifs, k)
            p_best = count_matrix(best_motifs, k)
        if p_motifs.max(0).sum() > p_best.max(0).sum():
            best_motifs = motifs.copy()
            
    return best_motifs


f = open('rosalind_ba2e.txt').readlines()
k, t = [int(i) for i in f[0].rstrip().split()]
dna = [i.strip() for i in f[1:]]

result = greedy_motifsearch_pseudocounts(dna, k, t)
print('\n'.join(result))
open('rosalind_ba2e_sub.txt', 'wt').write('\n'.join(result))

