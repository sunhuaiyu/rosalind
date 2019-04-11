#rosalind_ba5f
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

matrix = MatrixInfo.pam250

f = open('rosalind_ba5f.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()

alignments = pairwise2.align.localds(s, t, matrix, -5, -5)

a, b, s, i, j = alignments[0]
open('rosalind_ba5f_sub.txt', 'wt').write('\n'.join([str(int(s)), a[i:j], b[i:j]]))
