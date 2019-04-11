# rosalind_sset
# counting all subsets; powerset

powerset = 2**len(n) % 1000000


f = open('rosalind_seto.txt').read().replace('\n', '')

N = set(range(1, int(f.split('{')[0]) + 1))
A = set(array(f.split('{')[1].split('}')[0].split(',')).astype(int))
B = set(array(f.split('{')[-1].rstrip('}').split(',')).astype(int))


result = [A | B, A & B, A - B, B - A, N - A, N - B]
f = open('rosalind_seto_sub.txt', 'wt')
f.write('\n'.join([str(i) for i in result]))
f.close()
