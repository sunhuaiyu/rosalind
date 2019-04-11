# rosalind_ba1n
'''
Generate the d-Neighborhood of a String; Find all the neighbors of a pattern.
Given: A DNA string Pattern and an integer d.
Return: The collection of strings Neighbors(Pattern, d).
'''

from itertools import combinations, product
import numpy as np

f = open('rosalind_ba1n.txt')
s = f.readline().rstrip()
d = int(f.readline().rstrip())

p = np.array(list(product('ACGT', repeat=d)))
m = np.array(list(combinations(range(len(s)), d)))

out = []
for i in m:
    t = np.array(list(s))
    for j in p:
        t[i] = list(j)
        out.append(t.copy()) 

out = set(''.join(i) for i in out)

f = open('rosalind_ba1n_sub.txt', 'wt')
for i in out:
    f.write(i + '\n')
f.close()
