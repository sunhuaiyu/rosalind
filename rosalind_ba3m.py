#rosalind_ba3m

import networkx as nx 

def MaximalNonBranchingPaths(G):
    '''
    G: a networkx DiGraph
    '''
    paths = []
    for v in G.nodes():
        if G.in_degree(v) != 1 or G.out_degree(v) != 1:
            if G.out_degree(v) > 0:
                for i in G.out_edges(v):
                    non_branching_path = [*i]
                    w = i[1]
                    while G.in_degree(w) == 1 and G.out_degree(w) == 1:
                        u = G.out_edges(w)[0][1]
                        non_branching_path.append(u)
                        w = u
                    paths.append(non_branching_path)
    
    for cycle in nx.simple_cycles(G):
        branch = 0
        for v in cycle:
            if G.in_degree(v) != 1 or G.out_degree(v) != 1:
                branch = 1
        if branch == 0:
            cycle.append(cycle[0])
            paths.append(cycle)
    
    return paths
    
edges = []
for line in open('rosalind_ba3m.txt'):
    a, b = line.rstrip().split(' -> ')
    a = int(a)
    b = [int(i) for i in b.split(',')]
    for i in b:
        edges.append((a, i))

G = nx.DiGraph(data=edges)
result = '\n'.join([' -> '.join([str(i) for i in j]) for j in MaximalNonBranchingPaths(G)])
print(result)
open('rosalind_ba3m_sub.txt', 'wt').write(result)


