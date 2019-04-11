#rosalind_qrt
import numpy as np
from itertools import combinations

f = open('rosalind_qrt.txt')
species = f.readline().rstrip().split()
table = np.array([list(i.rstrip()) for i in f])

quartets = set()
for split in table:
    zeros = np.where(split=='0')[0]
    ones  = np.where(split=='1')[0]
    if len(zeros) >=2 and len(ones) >= 2:
        for i1, i2 in combinations(ones, 2):
            quartet1 = tuple(sorted([species[i1], species[i2]]))
            for j1, j2 in combinations(zeros, 2):
                quartet2 = tuple(sorted([species[j1], species[j2]]))
                quartets.add(tuple(sorted([quartet1, quartet2])))
                # series of sortings to ensure no redundant quartet added to quartets set

result = '\n'.join([str(i).replace("'", "").replace('((', '{').replace('), (', 
                '} {').replace('))', '}') for i in quartets])
print(result)
open('rosalind_qrt_sub.txt', 'wt').write(result)
