#rosalind_3sum
# had to rely on multiprocessing; can finish in time on the laptop

import numpy as np
from multiprocessing import Pool

def threeSum(arr):
    n = len(arr)
    S = sorted(arr)
    for i in range(n - 3):
        a = S[i]
        start = i + 1
        end = n - 1
        while start < end:
            b = S[start]
            c = S[end]
            if (a + b + c) == 0:
                result = sorted([arr.index(a)+1, arr.index(b)+1, arr.index(c)+1])
                return ' '.join(str(j) for j in result)
            elif (a + b + c) > 0:
                end -= 1
            else:          
                start += 1
    return '-1'

f = open('rosalind_3sum.txt')
k, n = [int(i) for i in f.readline().rstrip().split()]

A = [list(i) for i in np.fromfile(f, sep=' ', dtype=int).reshape(k, n)]

P = Pool(k)
open('rosalind_3sum_sub.txt', 'wt').write('\n'.join(list(P.map(threeSum, A))))

