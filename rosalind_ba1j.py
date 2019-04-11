# rosalind_ba1j

from itertools import product

def hamming(s, t):
    n = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            n += 1
    return n

def revc(s):
    pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(list(map(lambda n: pairs[n], s))[::-1])

f = open('rosalind_ba1j.txt')
s = f.readline().rstrip()
k, d = [int(i) for i in f.readline().rstrip().split()]

substrings = [s[i:i+k] for i in range(len(s) - k + 1)]
all_kmers = [ ''.join(i) for i in product('ATGC', repeat=k)]

counts = {i: 0 for i in all_kmers}

for i in all_kmers:
    for j in substrings:
        if hamming(i, j) <= d:
            counts[i] += 1
        if hamming(revc(i), j) <=d and i != revc(i):
            counts[i] += 1

out = ' '.join([i for i in counts.keys() if counts[i] == max(counts.values())]) 

open('rosalind_ba1j_sub.txt', 'wt').write(out)
