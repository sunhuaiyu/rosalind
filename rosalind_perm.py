# sun.huaiyu
# PERM

from itertools import permutations

n = int(open('rosalind_perm.txt').readline().rstrip())
p = list(permutations(range(1, n+1)))

print len(p)
for i in p:
    for k in i:
        print k,
    print '\n',


