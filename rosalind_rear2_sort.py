# rosalind_rear
# rosalind_sort

from itertools import permutations, combinations
import networkx as nx

one_reversal_ix = list(combinations(range(10), 2))
edges = dict()
for v in permutations(range(1, 11)):
    for i1, i2 in one_reversal_ix:
        permutated_v = v[:i1] + v[i1:i2+1][::-1] + v[i2+1:]
        pair = tuple(sorted([v, permutated_v]))
        if pair not in edges:
            edges[pair] = (i1, i2)

f = open('single_reversal_permutations.txt', 'wt')
for p, i in edges.items():
    f.write(str(p[0]) + '\t' + str(p[1]) + '\t' + str(i) +'\n')
f.close()
del edges
print('finished saving edgelist!')

# above code run forever, but in the end save graph data
###########################################################################
G = nx.Graph()
for line in open('single_reversal_permutations.txt'):
    v1, v2, label = [tuple([int(j) for j in i[1:-1].split(', ')]) 
                     for i in line.rstrip().split('\t')]
    G.add_edge(v1, v2, label=label)

print('finished constructing graph')

#rear
f = open('rosalind_rear.txt').read().rstrip()
data_set = [[tuple(int(i) for i in j.split()) for j in k.split('\n')] 
                                             for k in f.split('\n\n')]

result = [str(nx.shortest_path_length(G, *pair)) for pair in data_set]
print(' '.join(result))

#sort
f = open('rosalind_sort.txt').read().rstrip()
s1, s2 = [tuple(int(i) for i in j.split()) for j in f.split('\n')]

path = nx.shortest_path(G, s1, s2)
result2 = [str(len(path) - 1)]
for i in zip(path[:-1], path[1:]):
    result2.append(' '.join([str(i+1) for i in G[i[0]][i[1]]['label']]))
print('\n'.join(result2))

