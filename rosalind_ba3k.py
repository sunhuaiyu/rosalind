#rosalind_ba3k
# maximal non-branching paths
import networkx as nx

def MaximalNonBranchingPaths(G):
    '''
    G: a networkx DiGraph or MultiDiGraph; http://rosalind.info/problems/ba3m/
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

G = nx.MultiDiGraph()
f = open('rosalind_ba3k.txt')
for i in f:
    s = i.rstrip()
    G.add_edge(s[:-1], s[1:])

result = '\n'.join([''.join([i[0] for i in path[:-1]]) + path[-1]
                   for path in MaximalNonBranchingPaths(G)])

print(result)
open('rosalind_ba3k_sub.txt', 'wt').write(result)

    