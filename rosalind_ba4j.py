# rosalind_ba4j
def linearspectrum(peptide):
    aa_mass = {'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 
     'I': 113, 'H': 137, 'K': 128, 'M': 131, 'L': 113, 'N': 114, 'Q': 128, 
    'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}

    n = len(peptide)
    prefix_mass = np.array([0] + [aa_mass[i] for i in peptide]).cumsum()
    
    lin_spec = [0]
    for i in range(n):
        for j in range(i+1, n+1):
            lin_spec.append(prefix_mass[j] - prefix_mass[i])  
    return sorted(lin_spec)


peptide = open('rosalind_ba4j.txt').readline().rstrip()

f = open('rosalind_ba4j_ans.txt', 'wt')
f.write(' '.join(map(str, linearspectrum(peptide)))
f.close()
print(spectrum)
