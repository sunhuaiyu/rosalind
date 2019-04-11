#rosalind_sptd
'''
Define the split distance between two unrooted binary trees as the number of nontrivial 
splits contained in one tree but not the other.

Formally, if s(T1,T2) denotes the number of nontrivial splits shared by unrooted 
binary trees T1 and T2, Then their split distance is dsplit(T1,T2)=2(n−3)−2s(T1,T2).

Given: A collection of at most 3,000 species taxa and two unrooted binary trees T1 
and T2 on these taxa in Newick format.

Return: The split distance dsplit(T1,T2).
'''

import numpy as np
from Bio import Phylo
import networkx as nx
from io import StringIO

f = open('rosalind_sptd.txt')
species = f.readline().rstrip().split()
tree1 = Phylo.read(StringIO(f.readline().rstrip()), 'newick')
tree2 = Phylo.read(StringIO(f.readline().rstrip()), 'newick')

n = len(species)

#Constructing character table for the tree is just getting the leaves of each inner node.
#bipartition 
def character_table(tree):
    '''given a Bio.Phylo tree object, return character table showing 
    all nontrivial splits in a set of binary strings'''
    taxa = [i.name for i in tree.get_terminals()]
    n = len(taxa)
    
    internals = tree.get_nonterminals()
    internals.remove(tree.root) # remove the root node
    m = len(internals)
    table = np.zeros((m, n), int)
    for i in range(m):
        for j in internals[i].get_terminals():
            table[i, taxa.index(j.name)] = 1
        table[i] = (table[i, :] == table[i, 0])
    
    return set([''.join([str(i) for i in row]) for row in table])   

print(2 * (n-3) - 
      2 * len(character_table(tree1) & character_table(tree2)))

# older version need networkx graph
def character_table2(tree):
    '''given a Bio.Phylo tree object, return character table showing 
    all nontrivial splits in a set of binary strings'''
    terminals = sorted(tree.get_terminals(), key=lambda x: x.name)
    n = len(terminals)

    G = Phylo.to_networkx(tree)
    nontrivials = [(u, v) for u, v in G.edges() if (u.name is None) and (v.name is None)]
    m = len(nontrivials)
 
    table = np.zeros((m, n), dtype=int)
    for i in range(m):
        G.remove_edge(*nontrivials[i])
        s = nx.node_connected_component(G, terminals[0])
    
        for j in range(n):
            table[i, j] = int(terminals[j] in s)

        G.add_edge(*nontrivials[i])
    
    return set([''.join([str(i) for i in row]) for row in table]) 
