# sun.huaiyu
# LONG
from itertools import permutations
import networkx as nx

def overlap(seq1, seq2):
    n_overlap = 0
    for n in range(1, min([len(seq1), len(seq2)])):
        if seq1[-n:] == seq2[:n]:
            n_overlap = n
    return n_overlap

collection = dict()
for ln in open('rosalind_long.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

pairs = dict()
G = nx.MultiDiGraph()
for i, j in permutations(collection.keys(), 2):
    n = overlap(collection[i], collection[j])        
    if n >= (max(len(collection[i]), len(collection[j])) / 2) : 
        G.add_edge(i, j)
        pairs[(i, j)] = n

neighbors_5, neighbors_3 = [], []
assembled = []
superstrings = []

for next_pair in pairs.keys():
    print len(assembled),        

    if (neighbors_5 == []) and (neighbors_3 == []) and (len(assembled) != len(collection)):
        new_5, new_3 = next_pair
        contig = collection[new_5] + collection[new_3][pairs[next_pair]:]
        assembled = list(next_pair)
        print '\n'
    elif len(assembled) == len(collection) :
        superstrings.append(contig)
        new_5, new_3 = next_pair
        assembled = list(next_pair)
        print '\n'

    neighbors_5 = [(i, new_5) for i in G.predecessors(new_5) if i not in assembled]
    if len(neighbors_5) > 0:
        left = max(neighbors_5, key=lambda x: pairs[x])
        contig = collection[left[0]] + contig[pairs[left]:]
        new_5 = left[0]
        assembled.insert(0, new_5)
    neighbors_3 = [(new_3, i) for i in G.successors(new_3) if i not in assembled]
    if len(neighbors_3) > 0:
        right = max(neighbors_3, key=lambda x: pairs[x])
        contig = contig + collection[right[1]][pairs[right]:]
        new_3 = right[1]
        assembled.append(new_3)

shortest = min(superstrings, key=len)
f = open('rosalind_long_ans.txt', 'wt')
f.write(shortest)
f.close()
