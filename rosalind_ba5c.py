# rosalind_lcsq
# longest common subsequence

import numpy as np

f = open('rosalind_ba5c.txt')
a, b = [i.rstrip() for i in f.readlines()]

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

f = open('rosalind_ba5c_ans.txt', 'wt')
f.write(lcsq(a, b))
f.close()

