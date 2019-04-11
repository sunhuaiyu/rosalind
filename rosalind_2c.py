# sun.huaiyu
# 2c

aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
 'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

peptide = open('rosalind_2c.txt').readline().rstrip()

length = len(peptide)
wheel = [ peptide + peptide[:i] for i in range(length) ]

ions = [wheel[i][k:k+i+1] for i in range(length-1) for k in range(length)]
ions.append(peptide)

spectrum = [0] + sorted([sum([aa_mass[i] for i in p]) for p in ions]) 

f = open('rosalind_2c_ans.txt', 'wt')
f.write(' '.join(map(str, spectrum)))
f.close()
print spectrum
