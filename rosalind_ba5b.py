#rosalind_ba5b

import networkx as nx

#read data
f = open('rosalind_ba5b.txt').read().rstrip().split()
n = int(f[0])
m = int(f[1])

G = nx.DiGraph()
v = iter(f[2:])
for i in range(n):
    for j in range(m+1):
        w = int(next(v))
        G.add_edge((i, j), (i+1, j), weight=-w)
print(next(v))
for i in range(n+1):
    for j in range(m):
        w = int(next(v))
        G.add_edge((i, j), (i, j+1), weight=-w)

s, t = (0, 0), (n, m)
print(-nx.bellman_ford(G, s)[1][t])
