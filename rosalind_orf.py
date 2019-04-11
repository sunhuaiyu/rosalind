# sun.huaiyu
# PROT
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

sequence = ''
for l in open('rosalind_orf.txt'):
    if l[0] != '>':
        sequence = sequence + l.rstrip()       
revc = ''.join(map(lambda nt: pairs[nt], sequence)[::-1])

frames_all = [[sequence[i:i+3] for i in range(frame, len(sequence), 3)] 
                   for frame in range(3)]
frames_all.extend([[revc[i:i+3] for i in range(frame, len(revc), 3)] 
                   for frame in range(3)])

translation_all = [''.join([codon_aa.get(i) for i in f if len(i) == 3])
                      for f in frames_all]

translation = set()
for i in translation_all:
    peptide = i
    while ('M' in peptide) and ('*' in peptide):
        start = peptide.index('M')
        stop = peptide.index('*')
        if start < stop:
            translation.add(peptide[start:stop])
            peptide = peptide[start + 1:]
        if stop < start:
            peptide = peptide[stop + 1:]

f = open('rosalind_orf_ans.txt', 'wt')
f.write('\n'.join(list(translation)))
f.close()
