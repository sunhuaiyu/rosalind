# rosalind_ba1k

from itertools import product


f = open('rosalind_ba1k.txt')
s = f.readline().rstrip()
k = int(f.readline().rstrip())

substrings = [s[i:i+k] for i in range(len(s) - k + 1)]
all_kmers = sorted([ ''.join(i) for i in product('ATGC', repeat=k)])

out = ' '.join([str(substrings.count(i)) for i in all_kmers])

open('rosalind_ba1k_sub.txt', 'wt').write(out)

