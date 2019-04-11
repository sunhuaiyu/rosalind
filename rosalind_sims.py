#rosalind_sims

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio import SeqIO

# matrix = MatrixInfo.blosum62

s, t = [i.seq for i in SeqIO.parse('rosalind_sims.txt', 'fasta')]

alignments = pairwise2.align.globalms(s, t, 1, -1, -1, -1, penalize_end_gaps=False)

a, b, s, i, j = alignments[0]

while b[0] == '-':
    b = b[1:]
    a = a[1:]

b = b.rstrip('-')
a = a[: len(b)]

open('rosalind_sims_sub.txt', 'wt').write('\n'.join([str(int(s)), a, b]))

