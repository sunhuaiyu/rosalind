#rosalind_ba9k

def bwt_matrix(t):
    return sorted([t[i:] + t[:i] for i in range(len(t))])
    
def bwt(t):
    return ''.join([j[-1] for j in sorted([t[i:] + t[:i] for i in range(len(t))])])

def bwt_rev(s):
    w = list(s)
    m = sorted(w)
    while len(m[0]) < len(m):
        m = sorted([i + j for i, j in zip(w, m)])
    return m[0][1:] + '$'

def last_to_first(s, n):
    '''raw algorithm'''
    w = list(enumerate(s))
    m = sorted(w, key=lambda x: x[1])

    while len(m[0][1]) < len(m):
        m = sorted([(i[0], i[1] + j[1]) for i, j in zip(w, m)], key=lambda x: x[1])

    return [i[0] for i in m].index(n)

def last_to_first(s, n):
    import numpy as np
    return np.array(list(s)).argsort(kind='mergesort').argsort()[n]
    
def last_to_first(s, n):
    return sorted(range(len(s)), key=lambda x: s[x]).index(n)
        
f = open('rosalind_ba9k.txt')
s = f.readline().rstrip()
i = int(f.readline().rstrip())

print(last_to_first(s, i))

