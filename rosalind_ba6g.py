#rosalind_ba6g

def cycle_to_chromosome(nodes):
    n = len(nodes) // 2
    nodes.insert(0, 0) 
    chr = [0] * (n  + 1)
    for j in range(1, n + 1):
        if nodes[2 * j - 1] < nodes[ 2 * j ]:
            chr[j] = nodes[2 * j] // 2
        else:
            chr[j] = - nodes[2 * j - 1] // 2
    return chr[1:]
        

nodes = [int(i) for i in open('rosalind_ba6g.txt').readline().rstrip()[1:-1].split()]

signs = {1: '+', -1:''}
result = '(' + ' '.join(signs[i//abs(i)]+str(i) for i in cycle_to_chromosome(nodes)) + ')'
open('rosalind_ba6g_sub.txt', 'wt').write(result)