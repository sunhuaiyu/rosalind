# rosalind_ba2g
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


def gibbs_sampler(dna, k, t, N):

	# converting all kmers in dna into a matrix dna_m;
	# the shape of the matrix is (t, len(seq)-k+1, 4, k)
    dna_m = np.array([[kmer2matrix(j) for j in all_kmers(i, k)] for i in dna])

	#random draw from each row in dna
    draw = np.random.randint(len(dna[0])-k+1, size=t)
    motifs = dna_m[range(t), draw]

    score_best = motifs.sum(0).max(0).sum()
	
    for j in range(N):
        i = np.random.randint(t)        
        profile = (motifs[np.delete(np.arange(t), i)].sum(0) + 1) / (t + 4)
        
        p = np.product((dna_m[i] * profile).sum(1), axis=1)
        motifs[i] = dna_m[i, np.random.choice(len(p), p=p/p.sum())]
        
        score_motifs = motifs.sum(0).max(0).sum()
		
        if score_motifs > score_best:
            best_motifs = motifs
            score_best = score_motifs
			
    return score_best, [matrix2kmer(i) for i in best_motifs]


f = open('rosalind_ba2g.txt').readlines()
k, t, N = [int(i) for i in f[0].rstrip().split()]
dna = [i.strip() for i in f[1:]]

all_result = [gibbs_sampler(dna, k, t, N) for r in range(20)]
scores = np.array([i[0] for i in all_result])
result = '\n'.join(all_result[scores.argmax()][1])
print(result)
open('rosalind_ba2g_sub.txt', 'wt').write(result)

