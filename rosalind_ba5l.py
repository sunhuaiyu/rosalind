#rosalind_ba5l

from Bio import AlignIO 
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

blosum62 = MatrixInfo.blosum62

f = open('rosalind_ba5l.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()


aln = pairwise2.align.globalds(s, t, blosum62, -5, -5)

a, b, score, i, j = aln[0]
result = '\n'.join([str(int(score)), a, b])
print(result)
open('rosalind_ba5l_sub.txt', 'wt').write(result)
