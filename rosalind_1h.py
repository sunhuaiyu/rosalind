# sun.huaiyu
# 1h

import numpy as	np
from itertools import product, combinations
from multiprocessing import Pool
from datetime import datetime
global k_text, d, mutations
pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def mutagenesis(wildtype):
    mutants = []
    for i in mutations:
        c = wildtype.copy()
        c[i[0]] = i[1]
        mutants.append(''.join(c))
    return mutants

def mismatch(k_mer):
    hits = ((k_mer != k_text).sum(1) <= d).sum()
    return hits

print 'reading data ...'
f = open('rosalind_1h.txt')
text = f.readline().rstrip()
k, d = [int(i) for i in f.readline().split()]
f.close()
text_rc = ''.join(map(lambda nt: pairs[nt], text)[::-1])

print 'preparing mutations ...', datetime.now()
replacements = np.array(list(product('GATC', repeat=d)))
sites =	np.array(list(combinations(range(k), d)))
mutations = list(product(sites, replacements))

k_text = np.array([list(text[i:i+k]) for i in range(len(text) - k + 1)]
                 +[list(text_rc[i:i+k]) for i in range(len(text_rc) - k + 1)])

p = Pool(16)

print 'generating unique kmers ...', datetime.now()
kmers = np.array([list(oligo) for oligo in 
         {i for j in p.map(mutagenesis, k_text) for i in j}])

print 'counting mismatches ...', datetime.now()
c = np.array(p.map(mismatch, kmers))

print 'find most frequent ...', datetime.now()
most_freq = [''.join(i) for i in kmers[c == max(c)]]

f = open('rosalind_1h_ans.txt', 'wt')
f.write(' '.join(most_freq))
f.close()
