# sun.huaiyu
# REVP
def reverse_comp(sequence):
    pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    revc = ''.join(map(lambda nt: pairs[nt], sequence)[::-1])
    return revc

for ln in open('rosalind_revp.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        seq = ''        
    else:
        seq += line

f = open('rosalind_revp_ans.txt', 'wt')
for p in range(len(seq)):
    for i in range(4, 13):
        s = seq[p:p+i] 
        if (len(s) == i) and (s == reverse_comp(s)):
            f.write(str(p+1) + ' ' + str(i) + '\n')
f.close()

        