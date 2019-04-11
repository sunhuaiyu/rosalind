#rosalind_dbru

def revc2(sequence):
    return sequence.translate({65: 84, 67: 71, 71: 67, 84: 65})[::-1]

d = set()
for i in open('rosalind_dbru.txt'):
    s = i.rstrip()
    d.add((s[:-1], s[1:]))
    sc = revc2(s)
    d.add((sc[:-1], sc[1:]))

result = '\n'.join(['('+str(i[0])+', '+str(i[1])+')' for i in sorted(list(d))])
print(result)
open('rosalind_dbru_sub.txt', 'wt').write(result)

