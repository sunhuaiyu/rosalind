# sun.huaiyu
# REVC
pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}

sequence = open('rosalind_revc.txt').readline().rstrip()

revc = ''.join(map(lambda nt: pairs[nt], sequence)[::-1])

print revc
    