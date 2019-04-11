#rosalind_nwck
'''
Given: A collection of n trees (n≤40) in Newick format, with each tree containing
at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

Return: A collection of n positive integers, for which the kth integer represents 
the distance between xk and yk in Tk.
'''

from Bio import Phylo
from io import StringIO

c = open('rosalind_nwck.txt').read().rstrip().split('\n\n')

out = []
for i in c:
    t, x, y = i.split()
    tree = Phylo.read(StringIO(t), 'newick')
    ancestor = tree.common_ancestor(x, y)
    out.append(len(ancestor.get_path(x)) + len(ancestor.get_path(y)))

open('rosalind_nwck_sub.txt', 'wt').write(' '.join([str(i) for i in out]))
