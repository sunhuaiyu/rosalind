# sun.huaiyu
# 1B
pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}

sequence = open('rosalind_1b.txt').readline().rstrip()

revc = ''.join(map(lambda nt: pairs[nt], sequence)[::-1])

open('rosalind_1b_ans.txt', 'wt').write(revc)
    