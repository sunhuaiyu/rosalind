# sun.huaiyu
# HAMM

def dH(s, t):
    n = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            n += 1
    return n

f = open('rosalind_ba1g.txt')
s = f.readline().rstrip()
t = f.readline().rstrip()
if len(s) == len(t):
    print(dH(s, t))
else:
    print('Not equal length!')

