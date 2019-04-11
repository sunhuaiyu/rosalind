# rosalind_motz
# Motzkin numbers
# modulo arithmetic
# non-crossing perfect matching: a subset of perfect matching rosalind_pmch

from Bio import SeqIO, Seq

table = {'AU': 2, 'UA': 2, 'GC': 2, 'CG': 2, 'A': 1, 'U': 1, 'G': 1, 'C': 1, '':1}
def motz(s):  
    if s not in table:
        p = motz(s[1:])
        for i in range(1, len(s)):
            if (s[0] + s[i]) in ['AU', 'UA', 'GC', 'CG']:
                p += motz(s[1:i]) * motz(s[i+1:])            #the Catalan recursive form
        table[s] =  p % 1000000        
    return table[s]

seq = str((list(SeqIO.parse('rosalind_motz.txt', 'fasta'))[0]).seq)
print(motz(seq))

# Using dict instead of pandas.Series for the table appears faster.
# start with the basic table can be faster than a previously saved long table.