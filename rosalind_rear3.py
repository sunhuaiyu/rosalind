# rosalind_rear
# use scipy sparse matrix

import numpy as np
from math import factorial
from itertools import permutations, combinations
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.csgraph import shortest_path
import time

def permutation_to_lexicographic_ix(p):
    """
    Return the lexicographic index of the permutation `p` among all
    permutations of its elements. `p` must be a sequence and all elements
    of `p` must be distinct.
    """
    result = 0
    for j in range(len(p)):
        k = sum(1 for i in p[j + 1:] if i < p[j])
        result += k * factorial(len(p) - j - 1)
    return result

def one_reversal_graph(N):
    g = lil_matrix((factorial(N), factorial(N)), dtype=np.int8)

    for i, v in enumerate(permutations(range(1, N+1))):    
        for c in combinations(range(N), 2):
            permutated_v = v[:c[0]] + v[c[0]:c[1]+1][::-1] + v[c[1]+1:]       
            j = permutation_to_lexicographic_ix(permutated_v)
            if g[i, j] == 0:
                g[i, j] = 1
    return g

G = csr_matrix(one_reversal_graph(10))
dist_m = shortest_path(G, directed=0, unweighted=1)

# runs forever
###########################################################################

f = open('rosalind_rear.txt').read().rstrip()
data_set = [[tuple(int(i) for i in j.split()) for j in k.split('\n')] 
                                             for k in f.split('\n\n')]

pairs = np.array([list(map(permutation_to_lexicographic_ix, p)) for p in data_set])

result = [str(dist_m[p[0], p[1]]) for p in pairs]
print(' '.join(result))

