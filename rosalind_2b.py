# sun.huaiyu
# 2b

def revc(x):
    pairs = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([pairs[i] for i in x[::-1]])

def translate(dna_seq):
    codon_aa = {
 'CTT': 'L', 'ATG': 'M', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'AAC': 'N', 
 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'CTC': 'L', 'AGC': 'S', 'AAG': 'K', 
 'AGA': 'R', 'CAT': 'H', 'AAT': 'N', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L',
 'ACT': 'T', 'CAC': 'H', 'AAA': 'K', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 
 'CAA': 'Q', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'TGT': 'C', 'CGA': 'R', 
 'CAG': 'Q', 'TCT': 'S', 'GAT': 'D', 'CGG': 'R', 'TTT': 'F', 'TGC': 'C', 
 'GGG': 'G', 'TAG': '*', 'GGA': 'G', 'TAA': '*', 'GGC': 'G', 'TAC': 'Y', 
 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 
 'TCA': 'S', 'GCA': 'A', 'GTA': 'V', 'GCC': 'A', 'GTC': 'V', 'GCG': 'A', 
 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GCT': 'A', 'TGA': '*', 'GAC': 'D', 
 'CGT': 'R', 'TGG': 'W', 'GAA': 'E', 'CGC': 'R'}
    return ''.join([codon_aa[dna_seq[i: i+3]] 
                    for i in range(0, len(dna_seq), 3)])
         

f = open('rosalind_2b.txt')
dna = f.readline().rstrip()
peptide = f.readline().rstrip()
f.close()

size = len(peptide)
coding = set([dna[i:i+3*size] for i in range(len(dna) - 3*size + 1) 
        if (translate(dna[i:i+3*size]) == peptide) or 
           (translate(revc(dna[i:i+3*size])) == peptide) ])

f = open('rosalind_2b_ans.txt', 'wt')
f.write('\n'.join([i for i in coding]))
f.close()

