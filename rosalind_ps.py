#rosalind_ps

import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

f = open('rosalind_ps.txt')
n = int(f.readline().rstrip())
a = [int(i) for i in f.readline().rstrip().split()]
k = int(f.readline().rstrip())

result = [str(i) for i in heapsort(a)[:k]]
open('rosalind_ps_sub.txt', 'wt').write(' '.join(result))

