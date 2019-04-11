# rosalind_prob

from pylab import *


def rosalind_prob(s, a):
    return log10(((1-a)/2)**(s.count('A')+s.count('T'))*(a/2)**(s.count('G')+s.count('C'))).round(3)
    
f = open('rosalind_prob.txt', 'r')
t = f.readlines()
s = t[0].rstrip()
a = array(t[1].split()).astype(float)

x = rosalind_prob(s, a).tofile('rosalind_prob_sub.txt', sep=' ')

