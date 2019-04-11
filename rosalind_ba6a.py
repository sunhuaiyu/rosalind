#rosalind_ba6a
# Greedy Sort
'''
Given: A signed permutation P.
Return: The sequence of permutations corresponding to applying 
GreedySorting to P, ending with the identity permutation.

Sample Dataset
(-3 +4 +1 +5 -2)

Sample Output
(-1 -4 +3 +5 -2)
(+1 -4 +3 +5 -2)
(+1 +2 -5 -3 +4)
(+1 +2 +3 +5 +4)
(+1 +2 +3 -4 -5)
(+1 +2 +3 +4 -5)
(+1 +2 +3 +4 +5)

'''

import numpy as np
sign_dict = {1: '+', -1:'-'}

s = open('rosalind_ba6a.txt').readline().rstrip()[1:-1]
#s = '(-3 +4 +1 +5 -2)'[1:-1]
p = np.array(s.split(), int)

identity = np.arange(len(p)) + 1

result = []
i = 0
while (p != identity).any():
    while p[i] == i + 1:
        i += 1
    j = np.where(abs(p) == i+1)[0][0]
    p[i:j+1] = -1 * (p[i:j+1][::-1])

    line = '('+ ' '.join([sign_dict[np.sign(x)] + str(abs(x)) for x in p]) + ')'
    print(line)
    result.append(line)

open('rosalind_ba6a_sub.txt', 'wt').write('\n'.join(result))