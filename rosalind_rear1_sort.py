#rosalind_rear
#rosalind_sort

from itertools import permutations, combinations
import networkx as nx

all_permutations = list(permutations(range(1, 11)))
G = nx.Graph()
G.add_nodes_from(all_permutations)

one_reversal_ix = list(combinations(range(10), 2))

for i in all_permutations:
    for j1, j2 in one_reversal_ix:
        permutated_i = i[:j1] + i[j1:j2+1][::-1] + i[j2+1:]
        if not G.has_edge(i, permutated_i):
            G.add_edge(i, permutated_i, label=(j1, j2))

# nx.write_edgelist(G, 'rear_temp.txt')
# G = nx.read_edgelist('rear_temp.txt')

# in iPython, run above code before download input data (~ 30min)
###########################################################################

f = open('rosalind_rear.txt').read().rstrip()
data_set = [[tuple(int(i) for i in j.split()) for j in k.split('\n')] 
                                             for k in f.split('\n\n')]

result = [str(nx.shortest_path_length(G, *pair)) for pair in data_set]
print(' '.join(result))


f = open('rosalind_sort.txt').read().rstrip()
s1, s2 = [tuple(int(i) for i in j.split()) for j in f.split('\n')]

path = nx.shortest_path(G, s1, s2)
result2 = [str(len(path) - 1)]
for i in zip(path[:-1], path[1:]):
    result2.append(' '.join([str(i+1) for i in G[i[0]][i[1]]['label']]))
print('\n'.join(result2))
