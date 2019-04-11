#rosalind_nkew

from Bio import Phylo
from io import StringIO

c = open('rosalind_nkew.txt').read().rstrip().split('\n\n')

out = []
for i in c:
    t, x, y = i.split()
    tree = Phylo.read(StringIO(t), 'newick')
    out.append(int(tree.distance(x, y)))

open('rosalind_nkew_sub.txt', 'wt').write(' '.join([str(i) for i in out]))
