#rosalind_ms

f = open('rosalind_ms.txt')

n = int(f.readline().rstrip())
A = [int(j) for j in f.readline().rstrip().split()]

result = [str(i) for i in sorted(A)]
open('rosalind_ms_sub.txt', 'wt').write(' '.join(result))
