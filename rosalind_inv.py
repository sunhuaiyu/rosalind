#rosalind_inv
import numpy as np

def count_inversions(a):
    result = 0
    counts = [0] * (len(a)+1)
    rank = { v : i+1 for i, v in enumerate(sorted(a)) }
    for x in reversed(a):
        i = rank[x] - 1
        while i:
            result += counts[i]
            i -= i & -i
        i = rank[x]
        while i <= len(a):
            counts[i] += 1
            i += i & -i
    return result

f = open('rosalind_inv.txt')
n = int(f.readline().rstrip())
a = np.fromfile(f, sep=' ', dtype=int)

print(count_inversions(a))

