# sun.huaiyu
# rosalind_ba1a

import re

f = open('rosalind_ba1a.txt')
genome = f.readline().rstrip()
pattern = f.readline().rstrip()

matching = []
for i in range(len(genome)):
    if re.match(pattern, genome[i:]):
        matching.append(str(i))
print(len(matching))

# open('rosalind_1c_ans.txt', 'wt').write(' '.join(matching))
    