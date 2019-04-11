# sun.huaiyu
# LEXV
from itertools import product
from string import ascii_lowercase

f = open('rosalind_lexv.txt')
alphabet = f.readline().split()
n = int(f.readline().rstrip())

length = len(alphabet)
keys = list(ascii_lowercase[:length])
dictionary = dict(zip(keys, alphabet))

p = list(set([''.join(list(i)) for i in product([''] + keys, repeat=n)]))
p.sort()
q = [''.join([dictionary[k] for k in s]) for s in p[1:]]

f = open('rosalind_lexv_ans.txt', 'wt')
for i in q:
    f.write(i + '\n')
f.close()
