# rosalind_ba7b
'''
Limb Length Problem

Find the limb length for a leaf in a tree.

Given: An integer n, followed by an integer j between 0 and n - 1, 
followed by a space-separated additive distance matrix D (whose elements are integers).

Return: The limb length of the leaf in Tree(D) corresponding to row j of this 
distance matrix (use 0-based indexing).

'''
import numpy as np
from Bio.Phylo.TreeConstruction import _DistanceMatrix
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

f = open('rosalind_ba7b.txt')
n = int(f.readline().rstrip())
j = int(f.readline().rstrip())

D = np.fromfile(f, sep=' ', dtype=int).reshape(n, n)

#For the Phylo.TreeConstruction to work, integers must be Python int and not numpy.int64
dm = [[int(D[i, j]) for j in range(i+1)] for i in range(n)]
names = [str(i) for i in range(n)]

constructor = DistanceTreeConstructor()
tree = constructor.nj(_DistanceMatrix(names, dm))

print(round(tree.find_any(str(j)).branch_length))