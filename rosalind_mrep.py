#rosalind_mrep
import networkx as nx

def prefix(s):
    return [s[:i] for i in range(1, len(s) + 1)]        

def suffix(s):
    return [s[i:] for i in range(len(s))]     

def unique_prefix(str_list):
    return set.union(*(set(prefix(i)) for i in str_list))

def all_repeats(s, k=20):

    substrings = sorted(list(unique_prefix(suffix( s + '$' ))))

    # make a suffix trie 
    G = nx.DiGraph()
    prefix_dict = dict()
    end_node = 2
    for kmer in substrings:
        if len(kmer) == 1:
            begin_node = 1
        else:
            begin_node = prefix_dict[kmer[:-1]][1] 
        prefix_dict[kmer] = (begin_node, end_node)
        G.add_edge(begin_node, end_node, label=kmer[-1])
        end_node += 1

    collection = set()
    for v in G.nodes()[1:]:
        if G.out_degree(v) >= 2:
            path = nx.shortest_path(G, 1, v)
            if (len(path)-1 >= k) and (len(path)-1 <= len(s)//2):            
                repeat = ''.join([G[u][v]['label'] for u, v in zip(path[:-1], path[1:])])
                collection.add(repeat)
    return collection

s = open('rosalind_mrep.txt').readline().rstrip() 
n = len(s)

a = all_repeats(s)
b = {i[::-1] for i in all_repeats(s[::-1])}

result = '\n'.join(a & b)
print(result)
open('rosalind_mrep_sub.txt', 'wt').write(result)


