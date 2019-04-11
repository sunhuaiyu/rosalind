# sun.huaiyu
# FIBD_matrix
# not working with large integers

import numpy as np
def fibd_matrix(n, m):
    m1 = np.hstack((np.eye(m-1), np.zeros((m-1,1))))
    m2 = np.vstack((np.ones((1, m)), m1)).astype(np.uint64)
    m2[0, 0] = 0
    transition_matrix = np.matrix(m2)
    population_vector = np.matrix(np.zeros((m, 1))).astype(np.uint64)
    population_vector[0] = 1
    population = (transition_matrix **(n-1) * population_vector).sum()
    return population

n, m = open('rosalind_fibd.txt').readline().split()    
print fibd_matrix(int(n), int(m))
