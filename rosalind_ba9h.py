#rosalind_ba9h

def suffix_array(s, n):
    '''return with length'''
    return sorted([(s[i:], i) for i in range(n)], key=lambda x: x[0])

f = open('rosalind_ba9h.txt')
s = f.readline().rstrip()
patterns = [i.rstrip() for i in f.readlines()]


result = []
for i, j in suffix_array(s, len(s)):
    for p in patterns:
        if i[:len(p)] == p:
            result.append(str(j))

open('rosalind_ba9h_sub.txt', 'wt').write(' '.join(result))
