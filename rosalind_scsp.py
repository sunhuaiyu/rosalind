#rosalind_scsp
import numpy as np

def scsp(x, y): 
    '''find the shortest common supersequence of x and y'''
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
    wi = []
    while (i > 0) and (j > 0):
        if x[i-1] == y[j-1]:
            i -= 1
            j -= 1
            wi.insert(0, (i, j)) #the indices of the common subsequence
        else:
            if table[i, j-1] > table[i-1, j]:
                j -= 1
            else:
                i -= 1

    sc = ''
    j = (-1, -1)
    for i in wi:
        sc += x[j[0]+1:i[0]] + y[j[1]+1:i[1]] + x[i[0]]
        j = i
    sc += x[j[0]+1:] + y[j[1]+1:]          
    return sc


f = open('rosalind_scsp.txt')

s = f.readline().rstrip()
t = f.readline().rstrip()
result = scsp(s, t)
open('rosalind_scsp_sub.txt', 'wt').write(result)
print(result)
