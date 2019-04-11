# rosalind_sign

import pandas as pd
from itertools import product, permutations

def rosalind_sign(n):
    s = array(list(permutations(range(1, n+1))))
    signs = array(list(product([1, -1], repeat=n)))
    return  array([i*j for i in signs for j in s]).astype(int)


pd.DataFrame(rosalind_sign(6)).to_csv('rosalind_sign_sub.txt', sep=' ', 
                                   index=None, header=None)
                            