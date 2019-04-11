#rosalind_ba9d
import networkx as nx

def prefix(s):
    return [s[:i] for i in range(1, len(s) + 1)]        

def suffix(s):
    return [s[i:] for i in range(len(s))]     

def unique_prefix(str_list):
    return set.union(*(set(prefix(i)) for i in str_list))

s = open('rosalind_ba9d.txt').readline().rstrip() + '$'

all_prefix = sorted(list(unique_prefix(suffix(s))))

# make a suffix trie first
G = nx.DiGraph()
prefix_dict = dict()
end_node = 1
for kmer in all_prefix:
    if len(kmer) == 1:
        begin_node = 0
    else:
        begin_node = prefix_dict[kmer[:-1]][1] 
    prefix_dict[kmer] = (begin_node, end_node)
    G.add_edge(begin_node, end_node, label=kmer[-1])
    end_node += 1

# consolidate edges and remove 1-in 1-out nodes in the suffix trie
nodes_remain = G.nodes()
for v in nodes_remain:
    if G.out_degree(v) < 2: 
        if G.in_degree(v) == 1 and G.out_degree(v) == 1:
            u = G.predecessors(v)[0]
            w = G.successors(v)[0]
            G.add_edge(u, w, label=G[u][v]['label']+G[v][w]['label'])
            G.remove_node(v)

# find the longest repeat by going through all paths from root that 
# end with a node having >=2 out edges
result = ''
for v in [des for des in nx.descendants(G, 0) if G.out_degree(des) >= 2]:
    path = nx.shortest_path(G, source=0, target=v)
    #print(path)
    suffix = ''
    for u, v in zip(path[:-1], path[1:]):
        suffix += G[u][v]['label']
    if len(suffix) > len(result):
        result = suffix

'''
repeats = []
for v in G.nodes_iter():
    n = len([des for des in nx.descendants(G, v) if G.out_degree(des)==0])
    if n >= 2:
        path = nx.shortest_path(G, source=0, target=v)
        #print(path)
        suffix = ''
        for u, v in zip(path[:-1], path[1:]):
            suffix += G.get_edge_data(u, v)['label']
        repeats.append(suffix)
result = max(repeats, key=len)
'''
print(result)
open('rosalind_ba9d_sub.txt', 'wt').write(result)

