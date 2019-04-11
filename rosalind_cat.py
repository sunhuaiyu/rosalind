# rosalind_cat
# Catalan numbers
# modulo arithmetic
# non-crossing perfect matching: a subset of perfect matching rosalind_pmch

table = {'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1, '':1}
def cat(s):  
    if s not in table:
        p = 0
        for i in range(1, len(s), 2):
            if (s[0]+s[i]) in ['AU', 'UA', 'GC', 'CG']:
                p += cat(s[1:i]) * cat(s[i+1:])            #the Catalan recursive form
        table[s] =  p % 1000000        
    return table[s]

seq = ''.join([i.rstrip() for i in open('rosalind_cat.txt').readlines()[1:]])
print(cat(seq))

# using dict is much faster than pandas.Series

# the actual catalan number calculation
def catalan(n):
    c = [1]
    for i in range(0, n):
        p = 0
        for k in range(0, i + 1):
            p += c[k] * c[i-k]
        c.append(p % 1000000)
    return c[-1]

####
### cat('AU'*n) = catalan(n)

'''
table = Series({'AU': 1, 'UA': 1, 'GC': 1, 'CG': 1, '': 1, 
                'AA': 0, 'AG': 0, 'AC': 0, 'UU': 0, 'UG': 0, 'UC': 0, 
                'GA': 0, 'GU': 0, 'GG': 0, 'CA': 0, 'CU': 0, 'CC': 0})
def cat2(s):   # this one is slower
    table[s] = table.get(s, 
            sum([table[s[0]+s[i]] * cat(s[1:i]) * cat(s[i+1:]) 
                                  for i in range(1, len(s), 2)] ) % 1000000 )
    return table[s]
'''
