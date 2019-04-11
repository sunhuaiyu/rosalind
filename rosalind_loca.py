#rosalind_loca

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

matrix = MatrixInfo.pam250

collection = dict()
for ln in open('rosalind_loca.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

s, t = collection.values()

# somehow a gap penalty -0.5 minimize the hamming distance to edit distance
alignments = pairwise2.align.localds(s, t, matrix, -5, -5)

a, b, s, i, j = alignments[0]


open('rosalind_loca_sub.txt', 'wt').write('\n'.join([str(int(s)), 
                      a[i:j].replace('-', ''), b[i:j].replace('-', '')]))
