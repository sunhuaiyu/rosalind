# rosalind_ba3b

output = ''
for f in open('rosalind_ba3b.txt'):
    output += f[0]

output += f[1:].rstrip()
open('rosalind_ba3b_sub.txt', 'wt').write(output)



