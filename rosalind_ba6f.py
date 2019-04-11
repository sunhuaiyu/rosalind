#rosalind_ba6f

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

chr = [int(i) for i in open('rosalind_ba6f.txt').readline().rstrip()[1:-1].split()]

result = '(' + ' '.join(str(i) for i in chromosome_to_cycle(chr)) + ')'
open('rosalind_ba6f_sub.txt', 'wt').write(result)