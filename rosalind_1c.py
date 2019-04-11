# sun.huaiyu
# 1C
pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}

import re

f = open('rosalind_1c.txt')
pattern = f.readline().rstrip()
genome = f.readline().rstrip()

matching = []
for i in range(len(genome)):
    if re.match(pattern, genome[i:]):
        matching.append(str(i))

open('rosalind_1c_ans.txt', 'wt').write(' '.join(matching))
    