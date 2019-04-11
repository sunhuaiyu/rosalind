# sun.huaiyu
# LGIS
f = open('rosalind_lgis.txt')
length = int(f.readline().rstrip())
sequence = [int(i) for i in  f.readline().rstrip().split()]

def lgis(seq):
    incr_list = [[seq[0]]]
    for i in range(1, len(seq)):
        incr_list.append(max([incr_list[j] for j in range(i) 
                             if incr_list[j][-1] < seq[i]] or [[]], 
                             key=len) 
                         + [seq[i]])
    return max(incr_list, key=len)

f = open('rosalind_lgis_ans.txt', 'wt')
f.write(' '.join([str(i) for i in lgis(sequence)]))
f.write('\n')
f.write(' '.join([str(i) for i in lgis(sequence[::-1])[::-1]]))
f.close()


