#rosalind_smgb

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo
from Bio import SeqIO

# matrix = MatrixInfo.blosum62

s, t = [i.seq for i in SeqIO.parse('rosalind_smgb.txt', 'fasta')]

alignments = pairwise2.align.globalms(s, t, 1, -1, -1, -1, penalize_end_gaps=False)

a, b, s, i, j = alignments[0]

open('rosalind_smgb_sub.txt', 'wt').write('\n'.join([str(int(s)), a, b]))
