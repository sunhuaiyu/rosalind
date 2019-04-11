#rosalind_asmq

import numpy as np
a = [len(i.rstrip()) for i in open('rosalind_asmq.txt')]

values, counts = np.unique(a, return_counts=1)

b = values * counts
n = len(b)

N50 = 0
N75 = 0
for i in range(n):
    if sum(b[i:]) / sum(b) >= 0.75:  
        N75 = values[i]

    if sum(b[i:]) / sum(b) >= 0.5:
        N50 = values[i]

print(N50, N75)



