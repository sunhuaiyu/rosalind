# sun.huaiyu
# GRPH
from itertools import product
collection = dict()
for ln in open('rosalind_grph.txt'):
    line = ln.rstrip()       
    if line[0] == '>': 
        name = line[1:] 
        collection[name] = ''        
    else:
        collection[name] += line

adjacency = ''
for i, j in product(collection.keys(), repeat=2):
    if i != j and collection[i][-3:] == collection[j][:3]:
        adjacency += i + ' ' + j + '\n'

f = open('rosalind_grph_ans.txt', 'wt')
f.write(adjacency)
f.close()
