# rosalind_edit
# edit distance

import numpy as np

collection = dict()
for ln in open('rosalind_edit.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

a, b = collection.values()
from nltk.metrics import distance
print(distance.edit_distance(a, b))

# Wagner-Fischer algorithm
def edit_distance(s, t):
    m, n = len(s), len(t)
    d = np.zeros((m + 1, n + 1), dtype=int)
    d[:, 0] = np.arange(m + 1)
    d[0, :] = np.arange(n + 1)
    
    for j in np.arange(n):
        for i in np.arange(m):
            if s[i] == t[j]:
                d[i+1, j+1] = d[i, j]
            else:
                d[i+1, j+1] = min(d[i, j+1]+1, d[i+1, j]+1, d[i, j]+1)
    return d[m, n]
print(edit_distance(a, b))    
