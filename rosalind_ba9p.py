# rosalind_ba9p
'''
Tree Coloring Problem:
Color the internal nodes of a suffix tree given colors of the leaves.

Given: An adjacency list, followed by color labels for leaf nodes.
Return: Color labels for all nodes, in any order.
'''
import networkx as nx

f = open('rosalind_ba9p.txt').read().rstrip().split('\n-\n')

color_map = dict()
for line in f[1].split('\n'):
    k, v = line.split(': ')
    color_map[k] = v

G = nx.DiGraph()
node_colors = dict()

for line in f[0].split('\n'):
    u, children = line.split(' -> ')
    if children == '{}':
        G.add_node(u, color={color_map[u]})
    else:
        G.add_node(u, color=set())
        for v in children.split(','):
            G.add_edge(u, v)

colored = nx.get_node_attributes(G, 'color')
for v in nx.topological_sort(G, reverse=True)[:-1]:
    u = G.predecessors(v)[0]
    colored[u] |= colored[v]

result = []
for v in colored:
    if len(colored[v]) == 1:
        result.append(v + ': ' + list(colored[v])[0])
    else:
        result.append(v + ': purple')
    
open('rosalind_ba9p_sub.txt','wt').write('\n'.join(result))