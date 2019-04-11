# rosalind_mgap
import numpy as np
from Bio import SeqIO
from Bio import pairwise2

def lcsq(x, y):
    m = len(x)
    n = len(y)
    table = np.zeros((m+1, n+1), dtype=int)
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = max(table[i, j-1], table[i-1, j])
    
    i, j = m, n
    w = ''
    while (i > 0) and (j > 0):
        if x[i-1] == y[j-1]:
            w = x[i-1] + w
            i -= 1
            j -= 1
        else:
            if table[i, j-1] > table[i-1, j]:
                j -= 1
            else:
                i -= 1
    return w

s, t = [str(i.seq) for i in SeqIO.parse('rosalind_mgap.txt', 'fasta')]
aln = pairwise2.align.globalms(s, t, 100, -100, -0, -0)
a, b = aln[0][:2]
k = 0
for i in range(len(a)):
    if a[i] == '-' or b[i] == '-':
        k += 1
print(k)
# alternatively
print(len(s) + len(t) - 2* len(lcsq(s, t)))
