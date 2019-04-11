#rosalind_ba9c

import networkx as nx

def prefix(s):
    return [s[:i] for i in range(1, len(s) + 1)]        

def suffix(s):
    return [s[i:] for i in range(len(s))]     

def unique_prefix(str_list):
    return set.union(*(set(prefix(i)) for i in str_list))

s = open('rosalind_ba9c.txt').readline().rstrip()

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
result = nx.get_edge_attributes(G, 'label').values()

result = '\n'.join(result)
print(result)
open('rosalind_ba9c_sub.txt', 'wt').write(result)


