# rosalind_2sat
import networkx as nx
import numpy as np

def satisfying(scc):
    for c in scc:
        for i in range(len(c)-1):
            for j in range(i+1, len(c)):
                if c[i] == -c[j]: 
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
    scc = [np.array(list(i)) for i in nx.strongly_connected_components(G)]
    
    output = '0'            
    if satisfying(scc):
        assignment = []
        for i in range(len(scc)-1):
            if i in scc_ix:
                assignment += list(scc[i])
                scc_ix.remove(i)
                for j in range(i+1, len(scc)):
                    if j in scc_ix and sorted(np.abs(scc[i])) == sorted(np.abs(scc[j])):
                        scc_ix.remove(j)
        output = '1 ' + ' '.join([str(j) for j in sorted(assignment, key=abs)])
        
    result.append(output)         

  
result = '\n'.join(result)
print(result)
open('rosalind_2sat_sub.txt', 'wt').write(result)

