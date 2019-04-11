# rosalind_ba3c

def overlap_graph(dna):
    '''
    ix_linked: indices of dna strings already overlapping
    ix_remain: indices of dna strings not linked yet
    '''
    ix_linked = [0]
    ix_remain = list(range(1, len(dna)))
    
    i = 1
    while ix_remain != []:        
        if dna[i][:-1] == dna[ix_linked[-1]][1:]:
            ix_linked.append(i)
            ix_remain.remove(i)
            if ix_remain != []:
                i = ix_remain[0]
        elif dna[i][1:] == dna[ix_linked[0]][:-1]:
            ix_linked.insert(0, i)
            ix_remain.remove(i)
            if ix_remain != []:
                i = ix_remain[0]
        else:
            i += 1
    return ix_linked

dna = open('rosalind_ba3c.txt').read().split()

ix = overlap_graph(dna)
result = '\n'.join([dna[ix[i]] + ' -> ' + dna[ix[i+1]] for i in range(len(ix)-1)])
print(result)
open('rosalind_ba3c_sub.txt', 'wt').write(result)