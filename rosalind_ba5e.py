#rosalind_ba5e
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

blosum62 = MatrixInfo.blosum62

f = open('rosalind_ba5e.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()


# somehow a gap penalty -0.5 minimize the hamming distance to edit distance
alignments = pairwise2.align.globalds(s, t, blosum62, -5, -5)

a, b, s = alignments[0][0], alignments[0][1], int(alignments[0][2])

open('rosalind_ba5e_sub.txt', 'wt').write('\n'.join([str(s), a, b]))
