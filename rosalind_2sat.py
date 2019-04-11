# rosalind_2sat
import networkx as nx
import numpy as np

def satisfying(scc):
    for c in scc:
        cl = list(c)
        for i in range(len(c)-1):
            for j in range(i+1, len(c)):
                if cl[i] == -cl[j]: 
                    return False
    return True

f = open('rosalind_2sat.txt')
k = int(f.readline().rstrip())

result = []
for i in range(k):
    s = ''
    while s == '':
        s = f.readline().rstrip()
    n, m = [int(l) for l in s.split()]
    nodes = [i for i in range(1, n+1)] + [-i for i in range(1, n+1)]
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    
    for j in range(m):
        a, b = [int(l) for l in f.readline().rstrip().split()]
        G.add_edge(-a, b)
        G.add_edge(-b, a)
       
    scc_ix = nx.topological_sort(nx.condensation(G), reverse=True)
    scc = list(nx.strongly_connected_components(G))
    
    output = '0'            
    if satisfying(scc):
        assignment = []
        while scc_ix != []:
            assignment += list(scc[scc_ix[0]])
            for i in scc_ix[1:]:
                if sorted(map(abs, scc[scc_ix[0]])) == sorted(map(abs, scc[i])):
                    scc_ix.remove(i)
            scc_ix.pop(0)
        output = '1 ' + ' '.join([str(j) for j in sorted(assignment, key=abs)])
        
    result.append(output)         

  
result = '\n'.join(result)
print(result)
open('rosalind_2sat_sub.txt', 'wt').write(result)

