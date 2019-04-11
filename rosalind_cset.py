# rosalind_cset
'''
Problem
A submatrix of a matrix M is a matrix formed by selecting rows and columns 
from M and taking only those entries found at the intersections of the selected 
rows and columns. We may also think of a submatrix as formed by deleting 
the remaining rows and columns from M.

Given: An inconsistent character table C on at most 100 taxa.

Return: A submatrix of C′ representing a consistent character table on 
the same taxa and formed by deleting a single row of C. 
(If multiple solutions exist, you may return any one.)
'''

import numpy as np
import networkx as nx

def reverse_symbol(a):
    return (a == 0).astype(int)
        
table = open('rosalind_cset.txt').read().split()
mat = np.array([list(i.rstrip()) for i in table], dtype=int)
n = len(table)

G = nx.Graph()
for i in range(n-1):
    for j in range(1, n):
        a = mat[i] + mat[j]
        b = mat[i] + reverse_symbol(mat[j])
        if 0 in a and 2 in a and 0 in b and 2 in b:
            G.add_edge(i, j)

table.pop(nx.center(G)[0])           
open('rosalind_cset_sub.txt', 'wt').write('\n'.join(table))
