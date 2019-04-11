# sun.huaiyu
# LEXF
from itertools import product

f = open('rosalind_lexf.txt')
order = f.readline().split()
n = int(f.readline().rstrip())

p = [''.join(list(i)) for i in product(order, repeat=n)]

for i in p:
    print i

