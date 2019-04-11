#rosalind_ba11h
'''
Size of Spectral Dictionary Problem:
Find the size of the spectral dictionary for a given spectrum and score threshold.

Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.

Return: The size of the dictionary Dictionarythreshold(Spectrum').

Note: Use the provided max_score for the height of your table.
Your answer should be the number of peptides whose score is at least 
threshold and at most max_score.
'''

import numpy as np
import networkx as nx

def size_spec_dict_naive(spectrum, threshold, max_score):
    #this gives incomplete result, because a smaller peptide
    #can also score above threshold ??
    aa_masses = [57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186]
    m = len(spec)

    G = nx.DiGraph()
    G.add_nodes_from(range(m))
    for i in range(m-1):
        for j in range(i+1, m):
            if j - i in aa_masses:
                G.add_edge(i, j, {'weight': spec[j]})

    count = 0
    for path in nx.all_simple_paths(G, 0, m-1):
        score = sum([G[i][j]['weight'] for i, j in zip(path[:-1], path[1:])])
        if score >= threshold and score <= max_score:
            count += 1
    
    return count

def size_spec_dict(spectrum, threshold, max_score):
    '''
    Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
    Return: The size of the dictionary Dictionarythreshold(Spectrum'), i.e. the number
            of peptides that score in the range [threshold, max_score].'''

    aa_masses = [57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186]
    m = len(spectrum) #including 0
    
    #dynamic programming; size_table in shape (m, max_score+1)
    size_table = np.zeros((m, max_score * 2), dtype=int)
    size_table[0, 0] = 1
    
    for i in range(1, m):
        for t in range(max_score + 1):
            size_table[i, t] = sum([size_table[i - aa, t - spectrum[i]] 
                             for aa in aa_masses if i - aa >= 0 ])    
    
    return sum(size_table[-1][threshold:max_score])
    

f = np.fromfile('rosalind_ba11h.txt', sep=' ', dtype=int)
spec = np.array([0] + list(f[:-2]))
threshold = f[-2]
max_score = f[-1]

print(size_spec_dict(spec, threshold, max_score))




