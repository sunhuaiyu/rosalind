#rosalind_glob

from Bio import pairwise2
from Bio.SubsMat import MatrixInfo

blosum62 = MatrixInfo.blosum62

collection = dict()
for ln in open('rosalind_glob.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

s, t = collection.values()


alignments = pairwise2.align.globalds(s, t, blosum62, -5, -5)
print(alignments)

s = 0
for i in alignments:
    if i[2] > s:
        s = i[2]

print(int(s))