# rosalind_ba11j
'''
Spectral Alignment Problem:
Given a peptide and a spectral vector, find a modified variant of this peptide 
that maximizes the peptide-spectrum score among all variants of the peptides with 
up to k modifications.

Given: A peptide Peptide, a spectral vector Spectrum', and an integer k.
Return: A peptide Peptide' related to Peptide by up to k modifications with 
maximal score against Spectrum' out of all possibilities.
'''
import numpy as np

def peptide_vect(peptide):
    '''Given: A peptide, return it's prefix array (b-ions), including zero.'''

    aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
     'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
     'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 
     'Y': 163, 'X': 4, 'Z': 5}
     
    prefix = [peptide[:k] for k in range(len(peptide) + 1)] 
    return np.array([sum([aa_mass[k] for k in p]) for p in prefix], dtype=int)


def spectral_alignment(peptide_seq, spec_vect, k):
    '''Given: A peptide Peptide, a spectral vector Spectrum', and an integer k.
    Return: A peptide Peptide' related to Peptide by up to k modifications with 
    maximal score against Spectrum' out of all possibilities.'''
    
    peptide = peptide_vect(peptide_seq) #zero included
    
    #difference array
    diff_array = list([0, *np.diff(peptide)])

    # initiate dynamic programming 3D scoring table and path graph {node: predecessor}
    n = len(peptide)
    m = len(spec_vect)
    score_table = np.zeros((n, m, k+1), dtype=int)
    path_graph = dict()
    
    # the path graph in the first layer (layer 0) is a diagonal line 
    #that starts at (0, 0, 0), but not necessarily ends at (n - 1, m - 1, 0).    
    for i in range(1, n):
        if peptide[i] <= m - 1:
            path_graph[i, peptide[i], 0] = (i - 1, peptide[i-1], 0) 
            score_table[i, peptide[i], 0] = (spec_vect[peptide[i]] + 
                                             score_table[i - 1, peptide[i-1], 0])
    
    # build the remaining t[1:] layers, indicating >=1 PTMs
    for t in range(1, k+1):
        for i in range(1, n):
            for j in range(1, m):
                pred_nodes = [(i-1, s, t-1) for s in range(j)]
                
                if j >= diff_array[i]:
                    pred_nodes += [(i-1, j - diff_array[i], t)]
                
                path_graph[i, j, t] = max(pred_nodes, key=lambda x: score_table[x])
                score_table[i, j, t] = spec_vect[j] + score_table[path_graph[i, j, t]]
    
    # find the highest scored end point among [n-1, m-1, :], and trace back to [0, 0, :]
    v = (n - 1, m - 1, np.argmax(score_table[n-1, m-1, :]))
    best_path = []
    while v:
        best_path.append([peptide[v[0]], v[1]])
        v = path_graph.get(v)
    
    ptm_array = np.diff(np.diff(np.array(list(zip(*best_path[::-1])))), axis=0)[0]   
    
    #format output
    ptm_result = ''
    for i in range(n-1):
        if ptm_array[i] != 0:
            ptm_result += peptide_seq[i] + '({:+})'.format(ptm_array[i])
        else:
            ptm_result += peptide_seq[i]
    
    return ptm_result  #, score_table[n-1, m-1, :]


f = open('rosalind_ba11j.txt')
peptide_seq = f.readline().rstrip()
spec_vect = np.array([0] + f.readline().rstrip().split(), dtype=int) # add zero
k = int(f.readline().rstrip())
print(spectral_alignment(peptide_seq, spec_vect, k))
