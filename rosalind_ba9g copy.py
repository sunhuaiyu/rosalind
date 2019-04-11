#rosalind_ba9g

def suffix_array(s, n):
    '''return with length'''
    return sorted([(s[i:], i) for i in range(n)], key=lambda x: x[0])

s = open('rosalind_ba9g.txt').readline().rstrip()

result = str([i[1] for i in suffix_array(s, len(s))])[1:-1]
print(result)
open('rosalind_ba9g_sub.txt', 'wt').write(result)
