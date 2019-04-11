#rosalind_ba11i
'''
Probability of Spectral Dictionary Problem:
Find the probability of the spectral dictionary for a given spectrum and score threshold.

Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
Return: The probability of the dictionary Dictionarythreshold(Spectrum').
'''

import numpy as np
import networkx as nx

def probability_spec_dict(spectrum, threshold, max_score):
    '''
    Given: A spectral vector Spectrum', an integer threshold, and an integer max_score.
    Return: The probability of the dictionary Dictionarythreshold(Spectrum').'''

    aa_masses = [57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186]
    m = len(spectrum) #including 0
    
    #dynamic programming; size_table in shape (m, max_score+1)
    Pr_table = np.zeros((m, max_score * 2), dtype=float)
    Pr_table[0, 0] = 1.0
    
    for i in range(1, m):
        for t in range(max_score + 1):
            Pr_table[i, t] = sum([ Pr_table[i - aa, t - spectrum[i]] / 20 
                                     for aa in aa_masses if i - aa >= 0 ])    
    
    return sum(Pr_table[-1][threshold:max_score])
    

f = np.fromfile('rosalind_ba11i.txt', sep=' ', dtype=int)
spec = np.array([0] + list(f[:-2]))
threshold = f[-2]
max_score = f[-1]

print(probability_spec_dict(spec, threshold, max_score))




