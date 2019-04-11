#
import numpy as np

def change_making(coins, n):
    '''This function assumes that all coins are available infinitely.
    n is the number that we need to obtain with the fewest number of coins.
    coins is a list or tuple with the available denominations.'''

    m = np.zeros((len(coins) + 1, n + 1), dtype=int)
    m[0, :] = np.arange(n + 1)
    
    for c in range(1, len(coins) + 1):

        for r in range(1, n + 1):

            # Just use the coin coins[c - 1].
            if coins[c - 1] == r:
                m[c][r] = 1

            # coins[c - 1] cannot be included.
            # We use the previous solution for making r,
            # excluding coins[c - 1].
            elif coins[c - 1] > r:
                m[c][r] = m[c - 1][r]

            # We can use coins[c - 1].
            # We need to decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coins[c - 1]).
            # 2. Using the previous solution for making r - coins[c - 1] 
            #    (without using coins[c - 1]) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])

    return m[-1][-1]

f = open('rosalind_ba5a.txt')
n = int(f.readline().rstrip())
coins = np.array(f.readline().rstrip().split(',')).astype(int)
print(change_making(coins, n))