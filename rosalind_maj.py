# rosalind_maj

import numpy as np

f = open('rosalind_2sum.txt')
k, n = [int(i) for i in f.readline().rstrip().split()]

m = [i.rstrip().split() for i in f.readlines()]

result = []
for i in m:
    s = '-1'
    for j in range(n):
        if -i[j] in i:
            
            s = str(j+1) + ' ' + str(i.index(-i[j])+1)
            break
    result.append(s)

print(result)
open('rosalind_2sum_sub.txt', 'wt').write('\n'.join(result))
