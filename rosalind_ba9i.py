#rosalind_ba9i
# Burrows-Wheeler Transform

def bwt(t):
    return ''.join([j[-1] for j in sorted([t[i:] + t[:i] for i in range(len(t))])])
        
s = open('rosalind_ba9i.txt').readline().rstrip()

open('rosalind_ba9i_sub.txt', 'wt').write(bwt(s))
