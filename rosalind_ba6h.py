#rosalind_ba6h

def chromosome_to_cycle(chromosome):
    n = len(chromosome)
    nodes = [0] * (2 * n + 1)
    for j in range(1, n+1):
        i = chromosome[j-1]
        if i > 0:
            nodes[2 * j - 1] = 2 * i -1
            nodes[2 * j] = 2 * i
        else:
            nodes[2 * j - 1] = - 2 * i
            nodes[2 * j] = - 2 * i -1
    return nodes[1:]

def colored_edges(P):
    edges = []
    for chr in P:
        nodes = chromosome_to_cycle(chr)
        nodes = [0] + nodes + nodes[:1] 
        for j in range(1, len(chr)+1):
            edges.append((nodes[2 * j], nodes[2 * j + 1]))
    return edges

def colored_edges2(P):
    edges = set()
    for chr in P:
        nodes = chromosome_to_cycle(chr)
        nodes = [0] + nodes + nodes[:1] 
        for j in range(1, len(chr)+1):
            edges.add((nodes[2 * j], nodes[2 * j + 1]))
    return sorted(edges)


strings = open('rosalind_ba6h.txt').readline().rstrip()[1:-1].split(')(')
genome = [[int(i) for i in s.split()] for s in strings]

result = str(colored_edges(genome))[1:-1]
print(result)
open('rosalind_ba6h_sub.txt', 'wt').write(result)