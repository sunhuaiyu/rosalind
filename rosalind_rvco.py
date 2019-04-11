# rosalind_rvco
from Bio import SeqIO

def revc(s):
    pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(list(map(lambda n: pairs[n], s))[::-1])

seq = [str(i.seq) for i in SeqIO.parse(open('rosalind_rvco.txt'), 'fasta')]

n = 0
for s in seq:
    if s == revc(s):
        n += 1

print(n)
