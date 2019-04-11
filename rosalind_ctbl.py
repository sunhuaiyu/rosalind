#rosalind_ctbl
'''
Given: An unrooted binary tree T in Newick format for at most 200 species taxa.

Return: A character table having the same splits as the edge splits of T. 
The columns of the character table should encode the taxa ordered lexicographically; 
the rows of the character table may be given in any order. Also, for any given character, 
the particular subset of taxa to which 1s are assigned is arbitrary.
'''

import numpy as np
from Bio import Phylo
import networkx as nx

tree = Phylo.read(open('rosalind_ctbl.txt'), 'newick')
terminals = sorted(tree.get_terminals(), key=lambda x: x.name)
n = len(terminals)

G = Phylo.to_networkx(tree)
nontrivials = [(u, v) for u, v in G.edges() if (u.name is None) and (v.name is None)]
# nontrivial clades should have number of terminals > 1 (itself not a a terminal), 
# and < total number of terminals (not the root).
m = len(nontrivials)
 

result = np.zeros((m, n), dtype=int)
for i in range(m):
    G.remove_edge(*nontrivials[i])
    
    # A nontrivial edge ('character') partition all terminals into two sets
    # once a nontrivial edge is removed, the terminals is separated into 
    # two connected components, either with or without terminal[0]
    s = nx.node_connected_component(G, terminals[0])
    
    for j in range(n):
        result[i, j] = int(terminals[j] in s)

    G.add_edge(*nontrivials[i])


open('rosalind_ctbl_sub.txt', 'wt').write('\n'.join([''.join(i) 
                                          for i in result.astype(str)]))

    

