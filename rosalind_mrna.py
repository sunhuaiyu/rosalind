# sun.huaiyu
# MRNA
codon = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''

codon_table = dict(zip(codon.split()[0::2], codon.split()[1::2]))

codon_counts = dict()
for i in codon_table.keys():
    if codon_table[i] in codon_counts.keys():
        codon_counts[codon_table[i]] += 1
    else:
        codon_counts[codon_table[i]] = 1

protein = open('rosalind_mrna.txt').readline().rstrip()

product = 1
for residue in protein:
    product = product * codon_counts[residue] % 1000000
product = product * 3 % 1000000
print product
