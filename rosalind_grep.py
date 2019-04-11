#rosalind_grep

import networkx as nx

s = [i.rstrip() for i in open('rosalind_grep.txt')]
n = len(s)
# create de Bruijn graph
G = nx.DiGraph()
for i in range(n):
    for j in range(i+1, n):
        if s[i][1:] == s[j][:-1]:
            G.add_edge(i, j)
        elif s[i][:-1] == s[j][1:]:
            G.add_edge(j, i)
            
result = set()
for cycle in [c for c in nx.simple_cycles(G) if len(c)==n]:
    result.add(''.join([s[i][0] for i in cycle]))    

result = '\n'.join(result)
print(result)
open('rosalind_grep_sub.txt', 'wt').write(result)

