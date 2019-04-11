# sun.huaiyu
# FIB
def rabbits(n, k):
    adult, pup, parenting = 0, 1, 0
    for i in range(n):
        parenting = adult
        adult = adult + pup
        pup = k * parenting
    return adult

n, k = open('rosalind_fib.txt').readline().split()
print rabbits(int(n), int(k))
