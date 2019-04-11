# sun.huaiyu
# 1e

from multiprocessing import Pool

genome = open('rosalind_1e.txt').readline().rstrip()

length = len(genome)
prefix = []
for i in range(len(genome)):
    prefix.append(genome[:i])

def gc_count(seq):
    return seq.count('G') - seq.count('C')

p = Pool(16)
skew = p.map(gc_count, prefix)
skew_min = min(skew)

f = open('rosalind_1e_ans.txt','wt')
f.write(' '.join([str(i) for i in range(length) if skew[i] == skew_min]))
f.close()
