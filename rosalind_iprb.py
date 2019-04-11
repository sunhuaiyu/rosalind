# sun.huaiyu
# IPRB
def dominant(k, m, n):
    pr_k1st = float(k) / (k + m + n)
    pr_m1st = float(m) / (k + m + n) * (k + (m-1.0) * 0.75 + n * 0.5)/(k + m + n - 1)
    pr_n1st = float(n) / (k + m + n) * (k + m * 0.5) / (k + m + n - 1)
    return pr_k1st + pr_m1st + pr_n1st

f = open('rosalind_iprb.txt')
k, m, n = map(int, f.readline().split())
print dominant(k, m, n)
