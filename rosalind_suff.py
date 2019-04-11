#rosalind_suff
'''
Given a string s having length n, recall that its suffix tree T(s)
is defined by the following properties:

T(s) is a rooted tree having exactly n leaves.
Every edge of T(s) is labeled with a substring of s∗, where s∗
is the string formed by adding a placeholder symbol $ to the end of s.
Every internal node of T(s) other than the root has at least two children; 
i.e., it has degree at least 3.
The substring labels for the edges leading down from a node to its children 
must begin with different symbols.
By concatenating the substrings along edges, each path from the root to a 
leaf corresponds to a unique suffix of s∗.

Given: A DNA string s of length at most 1kbp.
Return: The substrings of s∗ encoding the edges of the suffix tree for s. 
'''
import networkx as nx

def prefix(s):
    return [s[:i] for i in range(1, len(s) + 1)]        

def suffix(s):
    return [s[i:] for i in range(len(s))]     

def unique_prefix(str_list):
    return set.union(*(set(prefix(i)) for i in str_list))

s = open('rosalind_suff.txt').readline().rstrip()

all_prefix = sorted(list(unique_prefix(suffix(s))))

# make a suffix trie first
G = nx.DiGraph()
prefix_dict = dict()
end_node = 2
for kmer in all_prefix:
    if len(kmer) == 1:
        begin_node = 1
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
open('rosalind_suff_sub.txt', 'wt').write(result)


