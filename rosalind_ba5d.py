#rosalind_ba5d

import networkx as nx

#read data
f = open('rosalind_ba5d.txt')
s = int(f.readline().rstrip())
t = int(f.readline().rstrip())

G = nx.DiGraph()
for line in f:
    l = line.rstrip().split('->')
    u  = int(l[0])
    v, w = map(int, l[1].split(':'))
    
    # sign-reverse weight, thus turn a longest path problem to
    # a shortest path search with bellman_ford
    G.add_edge(u, v, weight=-w)  

bf = nx.bellman_ford(G, s)
longest = -bf[1][t]
path = []
while t != None:
    path.append(t)
    t = bf[0][t]

path = path[::-1]

'''
longest = 0
path = []
for p in nx.all_simple_paths(G, s, t):
    len_p = 0
    for i in range(len(p) - 1):
        len_p += G[p[i]][p[i+1]]['weight']
    if len_p > longest:
        longest = len_p
        path = p
'''

print(longest)
print(path)
open('rosalind_ba5d_sub.txt', 'wt').write(str(longest)+'\n'+'->'.join(map(str,path)))