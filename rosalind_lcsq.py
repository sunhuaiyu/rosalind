# rosalind_lcsq
# longest common subsequence

import numpy as np

collection = dict()
for ln in open('rosalind_lcsq.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

a, b = collection.values()

def lcsq(x, y):
    m = len(x)
    n = len(y)
    table = np.zeros((m+1, n+1), dtype=int)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i, j-1], table[i-1, j])
    
    i, j = m, n
    w = ''
    while (i > 0) and (j > 0):
        if x[i-1] == y[j-1]:
            w = x[i-1] + w
            i -= 1
            j -= 1
        else:
            if table[i, j-1] > table[i-1, j]:
                j -= 1
            else:
                i -= 1
    return w

f = open('rosalind_lcsq_ans.txt', 'wt')
f.write(lcsq(a, b))
f.close()



def lcsq_table(x, y):
    m = len(x)
    n = len(y)
    table = np.zeros((m+1, n+1), dtype=int)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i, j-1], table[i-1, j])
    return table    

table = lcsq_table(a, b)


def lcsq(x, y, i, j): # this caused "maximum recursion depth exceeded in comparison"!
    if (i == 0) or (j == 0):
        return ''
    elif x[i-1] == y[j-1]:
        i -= 1
        j -= 1
        return lcsq(x, y, i, j) + x[i]    
    else:
        if table[i, j-1] > table[i-1, j]:
            j -= 1
        else:
            i -= 1
        return lcsq(x, y, i, j)


