#rosalind_ba9g

s = open('rosalind_ba9g.txt').readline().rstrip()

n = len(s)
suf = list(enumerate([s[i:] for i in range(n)]))
suf_sorted = sorted(suf, key=lambda a: a[1])

result = ', '.join([str(i[0]) for i in suf_sorted])
open('rosalind_ba9g_sub.txt', 'wt').write(result)