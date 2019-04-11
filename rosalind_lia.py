# sun.huaiyu
# LIA

from itertools import product
genotypes = {
('Aa', 'Aa'): [''.join(sorted(i)) for i in product('Aa', 'Aa')],
('AA', 'Aa'): [''.join(sorted(i)) for i in product('AA', 'Aa')],
('aa', 'Aa'): [''.join(sorted(i)) for i in product('aa', 'Aa')],
('Bb', 'Bb'): [''.join(sorted(i)) for i in product('Bb', 'Bb')],
('BB', 'Bb'): [''.join(sorted(i)) for i in product('BB', 'Bb')],
('bb', 'Bb'): [''.join(sorted(i)) for i in product('bb', 'Bb')]}

def children(parent):
    offspring = product(genotypes[(parent[0], 'Aa')], 
                        genotypes[(parent[1], 'Bb')])
    return list(offspring)


from scipy.misc import comb
def lia(k, N):
    p = sum([comb(2**k, i) * 0.25**i * 0.75**(2**k-i) 
             for i in range(N, 2**k+1)])    
    return p 
# correct answer, but not sure why.
