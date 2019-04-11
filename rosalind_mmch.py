# rosalind_mmch
# maximum matchings and RNA secondary structure

from scipy.misc import comb

fac_table = {0: 1}
def fac(n):
    if n not in fac_table:
        fac_table[n] = n * fac(n-1)
    return fac_table[n]


rna = ''.join([i.rstrip() for i in open('rosalind_mmch.txt').readlines()[1:]])

au_min, au_max = sorted((rna.count('A'), rna.count('U')))
gc_min, gc_max = sorted((rna.count('G'), rna.count('C')))

print( fac(au_max)//fac(au_max - au_min) * fac(gc_max) // fac(gc_max - gc_min))

# alternatively,
comb(au_max, au_min, exact=1) * fac(au_min) * comb(gc_max, gc_min, exact=1) * fac(gc_min)

