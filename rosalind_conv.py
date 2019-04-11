#rosalind_conv

import numpy as np
from itertools import product

x, y = open('rosalind_conv.txt').readlines()

x = np.array(x.split()).astype(float)
y = np.array(y.split()).astype(float)

d = np.array([abs(i[0] - i[1]) for i in product(x, y)])
d = np.sort(d)

dd = np.diff(d) < 0.000001
dd = dd.astype(int)

n = 0
ix = 0
i, l = 0, len(dd)
while i < l:
    c = 0
    while i < l and dd[i] == 1:
        c += 1
        i += 1
    if c > n:
        n = c
        ix = i
    i += 1

print(n+1, d[ix])        