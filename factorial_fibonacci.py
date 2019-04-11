# dynamic programming
# factorial
fac_table = {0: 1}
def fac(n):
    if n not in fac_table:
        fac_table[n] = n * fac(n-1)
    return fac_table[n]

# fib
fib_table = {0: 0, 1: 1}
def fib(n):
    if n not in fib_table:
        fib_table[n] = fib(n-1) % + fib(n-2)
    return fib_table[n]

# double factorial
fac2_table = {0: 1, 1: 1, 2: 2, 3: 3}
def fac2(n):
    k = n % 2
    while k < n + 2:
        fac2_table[k+2] = (k+2) * fac2_table[k]
        k += 2
    return fac2_table[n] % 1000000
    
