#rosalind_ba4h

import numpy as np
from collections import Counter

spec = sorted(np.fromfile('rosalind_ba4h.txt', sep=' ', dtype=int))

d = [j-i for j in spec[1:] for i in spec[:-1] if j > i]

c = Counter(d)

result = []
for i in sorted(c, key=lambda x: c[x])[::-1]:
    result += [str(i)] * c[i]

open('rosalind_ba4h_sub.txt', 'wt').write(' '.join(result))