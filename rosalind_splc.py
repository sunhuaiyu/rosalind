# sun.huaiyu
# SPLC
pairs = { 'A':'T', 'T':'A', 'G':'C', 'C':'G'}
rna_dna = {'A':'A', 'U':'T', 'C':'C', 'G':'G'}

codon_table = '''UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA *      CAA Q      AAA K      GAA E
UAG *      CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA *      CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G '''

codon = codon_table.split()[0::2]
codon_dna = [''.join([rna_dna[base] for base in c]) for c in codon]
amino_acid = codon_table.split()[1::2]

codon_aa = dict(zip(codon_dna, amino_acid))

seq = dict()
names = []
for ln in open('rosalind_splc.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:]
        seq[name] = ''
        names.append(name)        
    else:
        seq[name] += line

gene = seq[names[0]]
introns = [seq[i] for i in names[1:]]

for i in introns:
    pos, lenth = gene.index(i), len(i)
    gene = gene[:pos] + gene[pos+lenth:]

protein = ''
gene = gene[gene.index('ATG'):]
next_codon = 'ATG'
while codon_aa.get(next_codon) != '*':
    protein += codon_aa[next_codon]
    gene = gene[3:]
    next_codon = gene[:3]

f = open('rosalind_splc_ans.txt', 'wt')
f.write(protein)
f.close()
