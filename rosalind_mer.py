#rosalind_mer

f = open('rosalind_mer.txt')
n = int(f.readline().rstrip())
A = [int(i) for i in f.readline().rstrip().split()]
m = int(f.readline().rstrip())
B = [int(i) for i in f.readline().rstrip().split()]

C = []
while A != [] and B != []:
    a = A[0]
    b = B[0]
    if a <= b: 
        C.append(a)
        A.remove(a)
    else:
        C.append(b)
        B.remove(b)

if A == []:
    C += B
elif B == []:
    C += A

open('rosalind_mer_sub.txt', 'wt').write(' '.join([str(i) for i in C]))