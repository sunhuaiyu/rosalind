# sun.huaiyu
# 1A

import numpy as np

f = open('rosalind_1a.txt')
seq = f.readline().rstrip()
k = int(f.readline().rstrip())
f.close()

all_kmers = [seq[i:i+k] for i in range(len(seq) - k + 1)]
unique_kmers = np.array([i for i in set(all_kmers)])
all_kmers = np.array(all_kmers)
match_counts = np.array([(i == all_kmers).sum() for i in unique_kmers])
 

most_freq = unique_kmers[match_counts == max(match_counts)]

f = open('rosalind_1a_ans.txt', 'wt')
f.write(' '.join(most_freq))
f.close()

