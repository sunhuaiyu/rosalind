# rosalind_kmp
# failure array aka kmp_table
# Knuth-Morris-Pratt

w = ''.join([line.rstrip() for line in open('rosalind_kmp.txt').readlines()[1:]])
n = len(w)

t = np.zeros((n+1,), dtype=int)
pos = 2
cnd = 0
t[0] = -1
t[1] = 0
while pos < n:
    if w[pos-1] == w[cnd]:
        t[pos] = cnd + 1
        cnd += 1
        pos += 1
    elif cnd > 0:
        cnd = t[cnd]
    else:
        t[pos] = 0
        pos += 1

t[1:].tofile('rosalind_kmp_sub.txt', sep=' ')

