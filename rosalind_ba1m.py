# rosalind_ba1m
'''
Convert an integer to its corresponding DNA string.
Given: Integers index and k.
Return: NumberToPattern(index, k).
'''

d = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}

f = open('rosalind_ba1m.txt')
n = int(f.readline().rstrip())
w = int(f.readline().rstrip())

s = []
while len(s) < w:
    s.append(d[n % 4])
    n = n // 4

print(''.join(s[::-1]))


def lexicographic_ix_to_permutation(k, N=10):
    S = list(range(1, N+1))
    P = []
    while S != []:
        f = factorial(len(S)-1)
        i = int(floor(k/f))
        x = S[i]
        k = k%f
        P.append(x)
        S = S[:i] + S[i+1:]
    return P
