# rosalind_eval

import numpy as np

def rosalind_prob(s, a):
    return ((1-a)/2)**(s.count('A')+s.count('T')) * (a/2)**(s.count('G')+s.count('C'))

    
f = open('rosalind_eval.txt', 'r')
t = f.readlines()
n = np.float(t[0].rstrip())
s = t[1].rstrip()
a = np.array(t[2].rstrip().split()).astype(float)


out = rosalind_prob(s, a) * (n - len(s) + 1)

out.tofile('rosalind_eval_sub.txt', sep=' ')

 