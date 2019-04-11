#rosalind_ba9l
import numpy as np

def last_to_first(s):
    '''given a BW transformed string (last column), create a first-to-last mapping'''
    return sorted(range(len(s)), key=lambda x: s[x]) 
    # add np.argsort() to create last-to-first mapping

def BWTmatching(last_column, pattern):
    top = 0
    bottom = len(last_column) - 1
    
    # a 'last-to-first' mapping: 
    #ix_map = np.array(list(last_column)).argsort(kind='mergesort').argsort()
    ix_map = np.argsort(last_to_first(last_column))
    
    while top <= bottom:
        if pattern != '':
            symbol = pattern[-1]
            pattern = pattern[:-1]
            current_slice = last_column[top:bottom+1]
            if symbol in current_slice:
                top_ix = top + current_slice.find(symbol)
                bottom_ix = bottom - current_slice[::-1].find(symbol)
                top = ix_map[top_ix]
                bottom = ix_map[bottom_ix]
            else:
                return 0
        else:
            return bottom - top + 1
            
   
f = open('rosalind_ba9l.txt')
s = f.readline().rstrip()
patterns = f.readline().rstrip().split()

result = ' '.join([str(BWTmatching(s, p)) for p in patterns])

print(result)
open('rosalind_ba9l_sub.txt', 'wt').write(result)

