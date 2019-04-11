#rosalind_oap

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio import SeqIO


s, t = [i.seq for i in SeqIO.parse('rosalind_oap.txt', 'fasta')]

aln = pairwise2.align.globalms(s, t, 1, -2, -2, -2, penalize_end_gaps=False )

a, b, score, i, j = aln[0]

while b[0] == '-':
    b = b[1:]
    a = a[1:]
 
a = a.rstrip('-')
b = b[: len(a)]


open('rosalind_oap_sub.txt', 'wt').write('\n'.join([str(int(score)), a, b]))
