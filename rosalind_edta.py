#rosalind_edta
import numpy as np
from Bio import pairwise2

def hamming(seq1, seq2):
    # assert len(seq1) == len(seq2), 'unequal reads!'
    return sum([i[0] != i[1] for i in zip(seq1, seq2)])

collection = dict()
for ln in open('rosalind_edta.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

s, t = collection.values()


aln = pairwise2.align.globalxs(s, t, -0.5, -0.5)

l = 0
for i in aln:
    if i[-1] > l:
        a, b, l = i[0],i[1], i[-1]

result = '\n'.join([str(hamming(a, b)), a, b])
open('rosalind_edta_sub.txt', 'wt').write(result)
print(result)
