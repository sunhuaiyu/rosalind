#rosalind_ba3e

d = dict()
for l in open('rosalind_ba3e.txt'):
    i = l.rstrip()
    a, b = i[:-1], i[1:]
    if a in d.keys():
        d[a].append(b)
    else:
        d[a] = [b]


result = []
for i in sorted(d.keys()):
    result.append(str(i) + ' -> ' + ','.join(sorted(d[i])))


result = '\n'.join(result)
print(result)
open('rosalind_ba3e_sub.txt', 'wt').write(result)

