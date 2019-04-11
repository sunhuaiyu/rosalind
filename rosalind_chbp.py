# rosalind_chbp
'''
Given: A list of n species (n ≤ 80) and an n-column character 
table C in which the j-th column denotes the j-th species.
Return: An unrooted binary tree in Newick format that models C.
'''

from Bio import Phylo
from Bio.Phylo.TreeConstruction import _DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from io import StringIO
import re

# hamming distance
def hamming(seq1, seq2):
    # assert len(seq1) == len(seq2), 'unequal reads!'
    return int(sum([i[0] != i[1] for i in zip(seq1, seq2)]))

f = open('rosalind_chbp.txt')
species = f.readline().rstrip().split()
table = [''.join(i) for i in zip(*f.read().rstrip().split())]
n = len(table)

'''
For the Phylo.TreeConstruction to work, integers in the distance matrix
must be Python int and not numpy.int64
'''
dm = [[hamming(table[i], table[j]) for j in range(i+1)] for i in range(n)]
constructor = DistanceTreeConstructor()
tree = constructor.nj(_DistanceMatrix(names=species, matrix=dm))

handle = StringIO()
Phylo.write(tree, handle, format='newick', plain=True)
result = handle.getvalue()
result = re.sub('Inner[0-9]+', '', result)
open('rosalind_chbp_sub.txt', 'wt').write(result)
