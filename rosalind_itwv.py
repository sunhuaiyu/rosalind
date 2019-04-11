# rosalind_itwv
import numpy as np

def all_kmers(seq, k): 
	'''return the k-mer composition of a string'''
	return [seq[i:i+k] for i in range(len(seq) - k + 1)]

def can_interweave(km, s1, s2):
    while km != '':
        if km[0] == s1[:1]:
            s1 = s1[1:]
        elif km[0] == s2[:1]:
            s2 = s2[1:]
        else:
            return False
        km = km[1:]
    if (s1 == '') and (s2 == ''):
        return True
    return False

f = open('rosalind_itwv.txt', 'r').read().rstrip().split()
s = f[0]
f = f[1:]
n = len(f)
m = np.zeros((n, n), dtype=int)

for i in range(n):
    for j in range(i, n):
        k = len(f[i]) + len(f[j])
        for kmer in all_kmers(s, k):
            if can_interweave(kmer, f[i], f[j]) or can_interweave(kmer, f[j], f[i]):
                m[i, j] = 1
                m[j, i] = 1
                break

result = '\n'.join([' '.join([str(i) for i in row]) for row in m])
print(result)
open('rosalind_itwv_sub.txt', 'wt').write(result)

