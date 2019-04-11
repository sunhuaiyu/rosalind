#rosalind_ling

def suffix(s, n):
    '''return with length'''
    return sorted([(s[i:], n-i) for i in range(n)], key=lambda x: x[0])

def longest_common_prefix(a, b):
    k = 0
    while k < min(a[1], b[1]) and a[0][k] == b[0][k]:
        k += 1
    return k


s = open('rosalind_ling.txt').readline().rstrip()

n = len(s)
m = 4 + n * (n - 1) // 2

su = suffix(s, n)
count = su[0][1]
for i in range(1, n):
    count +=  su[i][1] - longest_common_prefix(su[i-1], su[i])

print(count/m)

    