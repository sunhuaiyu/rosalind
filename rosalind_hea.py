#rosalind_hea

import heapq

f = open('rosalind_hea.txt')
n = int(f.readline().rstrip())
a = [int(i) for i in f.readline().rstrip().split()]

heapq._heapify_max(a)
result = [str(i) for i in a]
open('rosalind_hea_sub.txt', 'wt').write(' '.join(result))
