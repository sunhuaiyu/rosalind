#rosalind_ba6b
# break points
'''
Find the number of breakpoints in a permutation.

Given: A signed permutation P.
Return: The number of breakpoints in P.

Sample Dataset
(+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)

Sample Output
8

'''

import numpy as np

s = '0 ' + open('rosalind_ba6b.txt').readline().rstrip()[1:-1]
p = np.array(s.split(), int)

print(sum(np.diff(p) != 1))
