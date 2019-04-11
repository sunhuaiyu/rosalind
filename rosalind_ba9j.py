#rosalind_ba9j
# Burrows-Wheeler Transform 
# Reverse
def bwt(t):
    return ''.join([j[-1] for j in sorted([t[i:] + t[:i] for i in range(len(t))])])

def bwt_rev(s):
    w = list(s)
    m = sorted(w)
    while len(m[0]) < len(m):
        m = sorted([i + j for i, j in zip(w, m)])
    return m[0][1:] + '$'
    
s = open('rosalind_ba9j.txt').readline().rstrip()
print(bwt_rev(s))


open('rosalind_ba9j_sub.txt', 'wt').write(bwt_rev(s))
