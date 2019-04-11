#rosalind_gaff
from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

blosum62 = MatrixInfo.blosum62

collection = dict()
for ln in open('rosalind_gaff.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

s, t = collection.values()

# somehow a gap penalty -0.5 minimize the hamming distance to edit distance
alignments = pairwise2.align.globalds(s, t, blosum62, -11, -1)

a, b, s = alignments[0][0], alignments[0][1], int(alignments[0][2])

open('rosalind_gaff_sub.txt', 'wt').write('\n'.join([str(s), a, b]))
