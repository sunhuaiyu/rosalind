#rosalind_hs

import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

f = open('rosalind_hs.txt')
n = int(f.readline().rstrip())
a = [int(i) for i in f.readline().rstrip().split()]

result = [str(i) for i in heapsort(a)]
open('rosalind_hs_sub.txt', 'wt').write(' '.join(result))

