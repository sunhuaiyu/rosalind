#rosalind_ba6j

def two_break_on_genome_graph(genome_graph, i, i1, j, j1):
    try:
        genome_graph[genome_graph.index((i, i1))] = (i, j)
    except:
        genome_graph[genome_graph.index((i1, i))] = (i, j)
    try:
        genome_graph[genome_graph.index((j, j1))] = (i1, j1)
    except:
        genome_graph[genome_graph.index((j1, j))] = (i1, j1)
    return genome_graph


f = open('rosalind_ba6j.txt')
strings = f.readline().rstrip()[1:-1].split('), (')
genome_graph = [tuple(int(i) for i in p.split(', ')) for p in strings]
i, i1, j, j1 = [int(i) for i in f.readline().rstrip().split(', ')] 

result = str(two_break_on_genome_graph(genome_graph, i, i1, j, j1))[1:-1]
print(result)
open('rosalind_ba6j_sub.txt', 'wt').write(result)
