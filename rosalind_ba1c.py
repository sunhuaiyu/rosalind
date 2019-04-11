# sun.huaiyu
# rosalind_ba1c
pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}

sequence = open('rosalind_ba1c.txt').readline().rstrip()

revc = ''.join(list(map(lambda n: pairs[n], sequence))[::-1])

open('rosalind_ba1c_ans.txt', 'wt').write(revc)
    