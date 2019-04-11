#rosalind_lrep
import networkx as nx

f = open('rosalind_lrep.txt')

s = f.readline().rstrip()
k = int(f.readline().rstrip())

G = nx.DiGraph()
for line in f:
    l = line.rstrip().split()
    #print(l)
    v1, v2, t_ix, t_len = int(l[0][4:]), int(l[1][4:]), int(l[2])-1, int(l[3])
    G.add_edge(v1, v2, label=s[t_ix : t_ix+t_len])

repeats = []
for v in G.nodes_iter():
    n = len([des for des in nx.descendants(G, v) if G.out_degree(des)==0])
    if n >= k:
        path = nx.shortest_path(G, source=1, target=v)
        #print(path)
        suffix = ''
        for u, v in zip(path[:-1], path[1:]):
            suffix += G.get_edge_data(u, v)['label']
        repeats.append(suffix)

print(max(repeats, key=len))
