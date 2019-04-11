# rosalind_ba2f
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

def matrix2kmer(m):
	'''
	Covert a (4, k) k-mer matrix in the order of 'ACGT' back to DNA sequence.
	'''
	d = {(1, 0, 0, 0): 'A', (0, 1, 0, 0): 'C', (0, 0, 1, 0): 'G', (0, 0, 0, 1): 'T'}
	return ''.join([ d[tuple(i)] for i in m.T ])


def randomized_motifsearch(dna, k, t, iteration):

	# converting all kmers in dna into a matrix dna_m;
	# the shape of the matrix is (t, len(seq)-k+1, 4, k)
	dna_m = np.array([[kmer2matrix(j) for j in all_kmers(i, k)] for i in dna])

	score_best = 0
	for r in range(iteration):
		#random draw from each row in dna
		draw = np.random.randint(0, high=len(dna[0])-k+1, size=t)
		motifs = dna_m[range(t), draw]
	
		while True:
			#compute a probability profile based on the k-mers randomly drawn 
			profile = (motifs.sum(0) + 1) / (t + 4)
		
			#select a new set of k-mers best-matching the profile
			motifs = dna_m[range(t), 
					 np.product((dna_m * profile).sum(2), axis=2).argmax(1)]

			score_motifs = motifs.sum(0).max(0).sum()
		
			if score_motifs > score_best:
				best_motifs = motifs
				score_best = score_motifs
			else:
				print(r, score_best, score_motifs)
				break

	return [matrix2kmer(i) for i in best_motifs]


f = open('rosalind_ba2f.txt').readlines()
k, t = [int(i) for i in f[0].rstrip().split()]
dna = [i.strip() for i in f[1:]]

result = '\n'.join(randomized_motifsearch(dna, k, t, 1000))
print(result)
open('rosalind_ba2f_sub.txt', 'wt').write(result)

