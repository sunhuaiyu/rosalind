# rosalind_ins
# insertion sort

file = open('rosalind_ins.txt').read().split('\n')
n = int(file[0])
a = [int(i) for i in file[1].split()]

ns = 0 #count for swaps
for i in range(1, n):
    k = i
    while k > 0 and a[k] < a[k -1]:
        s = a[k - 1]
        a[k - 1] = a[k]
        a[k] = s
        ns += 1
        k = k -1
print(ns)
