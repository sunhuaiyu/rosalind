#rosalind_ba6i

def cycle_to_chromosome(nodes):
    n = len(nodes) // 2
    nodes = [0] + nodes[:]
    chr = [0] * (n  + 1)
    for j in range(1, n + 1):
        if nodes[2 * j - 1] < nodes[ 2 * j ]:
            chr[j] = nodes[2 * j] // 2
        else:
            chr[j] = - nodes[2 * j - 1] // 2
    return chr[1:]

def graph_to_genome(genome_graph):
    signs = {1: '+', -1:''}    
    p = []
    nodes = []
    for v in genome_graph:
        nodes += v
        if v[0] > v[1]:
            nodes = nodes[1:] + nodes[:1]
            chr = cycle_to_chromosome(nodes)   
            p.append('(' + ' '.join(signs[i//abs(i)]+str(i) for i in chr) + ')')
            nodes = []
    return p

strings = open('rosalind_ba6i.txt').readline().rstrip()[1:-1].split('), (')
genome_graph = [[int(i) for i in p.split(', ')] for p in strings]

result = ''.join(graph_to_genome(genome_graph))
print(result)
open('rosalind_ba6i_sub.txt', 'wt').write(result)