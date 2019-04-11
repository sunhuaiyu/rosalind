#rosalind_root

fac2_table = {0: 1, 1: 1, 2: 2, 3: 3}
def fac2(n):
    k = n % 2
    while k < n + 2:
        fac2_table[k+2] = (k+2) * fac2_table[k]
        k += 2
    return fac2_table[n] % 1000000

def cunr(n):
    '''number of unrooted binary trees with n leaves'''
    return fac2(2 * n - 5)

def root(n):
    '''number of rooted binary trees with n leaves'''
    return cunr(n+1)

a = int(open('rosalind_root.txt').readline().rstrip())
print(cunr(a))
