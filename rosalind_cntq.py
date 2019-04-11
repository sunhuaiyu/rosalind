#rosalind_cntq
from scipy.misc import comb

f = open('rosalind_cntq.txt')
n = int(f.readline().rstrip())

print(comb(n, 4, exact=1) % 1000000)

