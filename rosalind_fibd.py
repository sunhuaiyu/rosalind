# sun.huaiyu
# FIBD
import numpy as np
def rabbits(n, m):
    life_span = np.zeros(m).astype(np.int64)
    life_span[0] = 1
    newborn = 0
    for i in range(n):
        live = life_span.sum()
        newborn = life_span[1:].sum()
        life_span[1:] = life_span[:-1].copy()        
        life_span[0] = newborn     
    return live

n, m = open('rosalind_fibd.txt').readline().split()
print rabbits(int(n), int(m))

