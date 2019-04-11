#rosalind_ba5k
# only works when there is no gap in the middle of t:s


from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

matrix = MatrixInfo.blosum62

s, t = [ln.rstrip() for ln in open('rosalind_ba5k.txt')]

aln = pairwise2.align.globalds(s, t, matrix, -5, -5)

a, b, score, i, j = aln[0]

j = len(t)//2
l = j + 1

n = b.find(t[j:j+5])
i = s.find(a[n:n+5])
k = i + 1 

print(str((i, j)) + ' ' + str((k, l)))