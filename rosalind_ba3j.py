#rosalind_ba3j
import networkx as nx

f = open('rosalind_ba3j.txt')
k, d = [int(i) for i in f.readline().rstrip().split()]
reads = [i.rstrip() for i in f]

G = nx.DiGraph()
n = len(reads)
G.add_nodes_from(range(n))

for i in range(n-1):
    for j in range(i+1, n):
        if reads[i][1:k] == reads[j][:k-1] and reads[i][-k+1:] == reads[j][-k:-1]:
            G.add_edge(i, j)
        if reads[j][1:k] == reads[i][:k-1] and reads[j][-k+1:] == reads[i][-k:-1]:
            G.add_edge(j, i)

ix = nx.dag_longest_path(G)
seq = [reads[i][0] for i in ix] + [reads[i][-1] for i in ix][- 2 * k - d + 1:]

open('rosalind_ba3j_sub.txt', 'wt').write(''.join(seq))
    
