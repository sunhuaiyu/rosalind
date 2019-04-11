# sun.huaiyu
# 1f

import numpy as np

f = open('rosalind_1f.txt')
pattern = f.readline().rstrip()
text = f.readline().rstrip()
d = int(f.readline().rstrip())
f.close()

pattern = np.array(list(pattern))
text = np.array(list(text))
window = len(pattern)

matched = []
for i in range(len(text) - window + 1):
    if sum(pattern != text[i : i + window]) <= d:
        matched.append(str(i))
        
f = open('rosalind_1f_ans.txt', 'wt')
f.write(' '.join(matched))
f.close()
