# rosalind_sseq

f = open('rosalind_sseq.txt', 'r').readlines()
s, t = f[1], f[3]

output = []
k = 0
for i in t:
    for j in range(k, len(s)):
        if i == s[j]:
            output.append(j)
            k = j + 1
            break

output = array(output) + 1
output.tofile('rosalind_sseq_sub.txt', sep=' ')

        