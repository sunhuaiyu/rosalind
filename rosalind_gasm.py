#rosalind_gasm

import networkx as nx

def revc2(sequence):
    '''translate ACGT to TGCA based on ASCII code; return reversed sequence'''
    return sequence.translate({65: 84, 67: 71, 71: 67, 84: 65})[::-1]

def all_kmers(seq, n, k): 
	'''return the k-mer composition of a string'''
	return [seq[i:i+k] for i in range(n - k + 1)]

s = [i.rstrip() for i in open('rosalind_gasm.txt')]
n = len(s[0])
s = s + list(map(revc2, s))

# try de Bruijn graph with k >= 3
k = n - 1
result = ''
while k >= 3:
    G = nx.DiGraph()

    for u in s:
        all_k = all_kmers(u, n, k)
        G.add_edges_from(zip(all_k[:-1], all_k[1:]))

    cycles = list( nx.simple_cycles(G) )
    if len(cycles) == 2 and len(cycles[0]) == G.order() / 2:
        result = ''.join([i[0] for i in cycles[0]])
        break

    k -= 1

print(result)
open('rosalind_gasm_sub.txt', 'wt').write(result)

