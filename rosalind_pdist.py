# rosalind_pdst
# hamming distance

import pandas as pd
from scipy.spatial.distance import pdist, squareform

d = {'A': 1, 'T': 2, 'G': 3, 'C': 4}

frame = dict()
names = []
for l in open('rosalind_pdst.txt'):
    line = l.rstrip()       
    if line[0] == '>':
        id = line 
        names.append(id) 
        frame[id] = ''        
    else:
        frame[id] += line

b = array([[d[j] for j in frame[i]] for i in names])

x = squareform(pdist(b, 'hamming'))
pd.DataFrame(x).to_csv('rosalind_pdst_sub.txt', index=None, header=None, sep=' ')
