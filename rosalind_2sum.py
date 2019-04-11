#rosalind_2sum

import numpy as np

f = open('rosalind_2sum.txt')
k, n = [int(i) for i in f.readline().rstrip().split()]

m = [[int(j) for j in i.rstrip().split()] for i in f.readlines()]

result = []
for i in range(k):
    s = '-1'
    for j in range(n):
        a = m[i][j]
        for x in range(j+1, n):
            if -a == m[i][x]:       
                s = str(j+1) + ' ' + str(x+1)
                break
        if s != '-1':
            break
    result.append(s)

print(result)
open('rosalind_2sum_sub.txt', 'wt').write('\n'.join(result))
