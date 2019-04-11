# rosalind_ba2d
import numpy as np

def all_kmers(seq, k): # to find the k-mer composition of a string
	return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def kmer2matrix(kmer):
	'''
	Covert a single k-mer to a (4, k) matrix in the order of 'ACGT'.
	'''
	d = {'A':[1, 0, 0, 0], 'C':[0, 1, 0, 0], 'G':[0, 0, 1, 0], 'T':[0, 0, 0, 1]}
	return np.array([d[i] for i in kmer]).T

def matrix2kmer(m):
	'''
	Covert a (4, k) k-mer matrix in the order of 'ACGT' back to DNA sequence.
	'''
	d = {(1, 0, 0, 0): 'A', (0, 1, 0, 0): 'C', (0, 0, 1, 0): 'G', (0, 0, 0, 1): 'T'}
	return ''.join([ d[tuple(i)] for i in m.T ])

def greedy_motifsearch(dna, k, t):

	# converting all kmers in dna into a matrix dna_array;
	# the shape of the matrix is (t, len(seq)-k+1, 4, k)
	dna_array = np.array([[kmer2matrix(j) for j in all_kmers(s, k)] for s in dna])

	best_motifs = dna_array[:, 0]

	for kmer in dna_array[0]:
		motifs = np.array([kmer])
	
		for i in range(1, t):
			profile = motifs.sum(0) / t
			matching_ix = np.product((dna_array[i] * profile).sum(1), axis=1).argmax()
			motifs = np.append(motifs, [dna_array[i, matching_ix]], axis=0)

		if motifs.sum(0).max(0).sum() > best_motifs.sum(0).max(0).sum():
			best_motifs = motifs.copy()

	return [matrix2kmer(i) for i in best_motifs]


f = open('rosalind_ba2d.txt').readlines()
k, t = [int(i) for i in f[0].rstrip().split()]
dna = [i.strip() for i in f[1:]]
 
result = greedy_motifsearch(dna, k, t)
print('\n'.join(result))
open('rosalind_ba2d_sub.txt', 'wt').write('\n'.join(result))

