# rosalind_eval

import numpy as np
from scipy.misc import comb
    
f = open('rosalind_indc.txt', 'r')
t = f.readlines()
n = 2 * np.int(t[0].rstrip())



out = np.log10(np.array([comb(n, i, exact=1) * .5**n 
                                  for i in range(n+1)]).cumsum()[::-1])[1:]

out.tofile('rosalind_indc_sub.txt', sep=' ')

