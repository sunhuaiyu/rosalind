# rosalind_aspc

import numpy as np

from scipy.misc import comb

f = lambda n, m: sum([comb(n, i, exact=1)%1000000 for i in range(m, n+1)])

f(1739, 819)%1000000  
# 154544