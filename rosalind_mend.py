#rosalind_mend
from Bio import Phylo
import numpy as np

ancesters = {'AA': np.array([1, 0, 0]),
             'Aa': np.array([0, 1, 0]),
             'aa': np.array([0, 0, 1])}            

def gamete_pool(p):
    return np.array([[p[0], p[1]/2], [p[1]/2, p[2]]]).sum(0)

def offspring(x, y):
    '''x, y are [AA, Aa, aa] probability array'''
    cross = np.outer(gamete_pool(x), gamete_pool(y)) 
    p = np.array([cross[0][0], cross[0][1] + cross[1][0], cross[1][1]])
    p = p / p.sum()
    return p

tree = Phylo.read(open('rosalind_mend.txt'), 'newick')
for i in tree.get_terminals():
    i.name = ancesters[i.name]

while tree.count_terminals() > 1:
    for i in tree.get_nonterminals():
        if i.is_preterminal():
            x, y = i.get_terminals()
            i.name = offspring(x.name, y.name)
            tree.collapse(x)
            tree.collapse(y)

print(tree.root.name)
