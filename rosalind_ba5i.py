#rosalind_ba5i

from Bio import pairwise2

v, w = [ln.rstrip() for ln in open('rosalind_ba5i.txt')]

aln = pairwise2.align.globalms(v, w, 1, -2, -2, -2, penalize_end_gaps=False)

a, b, score, i, j = aln[0]

while b[0] == '-':
    b = b[1:]
    a = a[1:]
 
a = a.rstrip('-')
b = b[: len(a)]

open('rosalind_ba5i_sub.txt', 'wt').write('\n'.join([str(int(score)), a, b]))
