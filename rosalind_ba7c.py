# rosalind_ba7c
'''
Additive Phylogeny Problem

Construct the simple tree fitting an additive matrix.

Given: n and a tab-delimited n x n additive matrix.
Return: A weighted adjacency list for the simple tree fitting this matrix.

Note on formatting: The adjacency list must have consecutive integer node labels 
starting from 0. The n leaves must be labeled 0, 1, ..., n-1 in order of
their appearance in the distance matrix. Labels for internal nodes may be 
labeled in any order but must start from n and increase consecutively.
'''

import numpy as np
from Bio.Phylo.TreeConstruction import _DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
from Bio import Phylo

f = open('rosalind_ba7c.txt')
n = int(f.readline().rstrip())

D = np.fromfile(f, sep=' ', dtype=int).reshape(n, n)

#For the Phylo.TreeConstruction to work, integers must be Python int and not numpy.int64
dm = [[int(D[i, j]) for j in range(i+1)] for i in range(n)]
names = [str(i) for i in range(n)]

constructor = DistanceTreeConstructor()
tree = constructor.nj(_DistanceMatrix(names, dm))
for v in tree.find_clades():
    if 'Inner' in v.name:
        v.name = str(n + int(v.name[5:]) - 1)

G = Phylo.to_networkx(tree)
result = []
for u, v in G.edges():
    if u.is_parent_of(v):
        w = int(round(v.branch_length))
    else:
        w = int(round(u.branch_length))
    result.append([u.name, v.name, str(w)])
    result.append([v.name, u.name, str(w)])

result = sorted(result, key=lambda x: int(x[0]))
result = [i[0] + '->' + i[1] + ':' + i[2] for i in result]
open('rosalind_ba7c_sub.txt', 'wt').write('\n'.join(result))
