#rosalind_ptra

from Bio.Seq import Seq

dna, protein = [i.rstrip() for i in open('rosalind_ptra.txt')]

dna = Seq(dna)

T = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26]
for t in T:
    translation = dna.translate(table=t, stop_symbol='')
    if str(translation) == protein:
        print(t)
        
