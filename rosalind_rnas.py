# rosalind_rnas
# Motzkin numbers with modification


table = {'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1, 'UG': 1, 'GU': 1,
          'A': 1, 'U': 1, 'G': 1, 'C': 1, '':1}

def motz2(s):  
    if s not in table:
        p = motz2(s[1:])
        for i in range(4, len(s)):
            if (s[0] + s[i]) in ['AU', 'UA', 'GC', 'CG', 'UG', 'GU']:
                p += motz2(s[1:i]) * motz2(s[i+1:])            #the Catalan recursive form
        table[s] =  p       
    return table[s]

seq = open('rosalind_rnas.txt').readline().rstrip()
print(motz2(seq))

