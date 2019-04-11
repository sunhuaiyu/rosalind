# rosalind_ba1h

def hamming(s, t):
    n = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            n += 1
    return n


f = open('rosalind_ba1h.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()
d = int(f.readline().rstrip())

k = len(s)

pos = ' '.join([str(i) for i in range(len(t) - k + 1) if hamming(t[i:i+k], s) <= d])

open('rosalind_ba1h_sub.txt', 'wt').write(pos)

