#rosalind_ba5h

from Bio import pairwise2

v, w = [ln.rstrip() for ln in open('rosalind_ba5h.txt')]

aln = pairwise2.align.globalms(v, w, 1, -1, -1, -1, penalize_end_gaps=False)

a, b, score, i, j = aln[0]

while b[0] == '-':
    b = b[1:]
    a = a[1:]
 
b = b.rstrip('-')
a = a[: len(b)]


open('rosalind_ba5h_sub.txt', 'wt').write('\n'.join([str(int(score)), a, b]))
