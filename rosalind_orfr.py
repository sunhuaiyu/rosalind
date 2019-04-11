#rosalind_orfr

from Bio.Seq import Seq

dna = open('rosalind_orfr.txt').readline().rstrip()

c = [Seq(dna), Seq(dna).reverse_complement()]

orfs = []
for i in [0, 1]:
    start = 0
    while start != -1:
        start = c[i].find('ATG')
        c[i] = c[i][start:]
       
        orfs.append(c[i][:-(len(c[i])%3)].translate(table=1, to_stop=True))
        c[i] = c[i][start+3:]
            
open('rosalind_orfr_sub.txt', 'wt').write(str(max(orfs, key=len)))        
