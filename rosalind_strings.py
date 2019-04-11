# multiple alignment algorithms in Python

from collections import defaultdict
from itertools   import combinations

import arrays
import distance


MATCH    =  0
MISMATCH = -1
GAP      = -1


def basic_alignment_table(s, t):
    m = len(s)
    n = len(t)

    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = GAP * i

    for j in range(1, n + 1):
        T[0][j] = GAP * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[i][j] = max(T[i - 1][j - 1] + (MATCH if s[i - 1] == t[j - 1] else MISMATCH), T[i - 1][j] + GAP, T[i][j - 1] + GAP)

    return T


def basic_alignment(s, t):
    m   = len(s)
    n   = len(t)

    T   = basic_alignment_table(s, t)
    e_d = -T[m][n]

    s_a = []
    t_a = []

    while m + n > 0:
        if T[m][n] == T[m - 1][n] + GAP:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] + GAP:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + (MATCH if s[m - 1] == t[n - 1] else MISMATCH):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def count_basic_alignments(s, t):
    m = len(s)
    n = len(t)

    T = basic_alignment_table(s, t)
    V = defaultdict(int)

    def alignments(m, n):
        if m != 0 and n != 0:
            if (m, n) not in V:
                total = 0
                if T[m][n] == T[m - 1][n] + GAP:
                    total += alignments(m - 1, n)
                if T[m][n] == T[m][n - 1] + GAP:
                    total += alignments(m, n - 1)
                if T[m][n] == T[m - 1][n - 1] + (MATCH if s[m - 1] == t[n - 1] else MISMATCH):
                    total += alignments(m - 1, n - 1)
                V[(m, n)] = total
            return V[(m, n)]
        else:
            return 1

    return alignments(m, n)


def mismatch_alignment_table(s, t):
    m = len(s)
    n = len(t)

    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = -i

    for j in range(1, n + 1):
        T[0][j] = -j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[i][j] = max(T[i - 1][j - 1] + (1 if s[i - 1] == t[j - 1] else -1), T[i - 1][j] - 1, T[i][j - 1] - 1)

    return T


def semi_global_alignment_table(s, t):
    m = len(s)
    n = len(t)

    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    M = (0, m, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[i][j] = max(T[i - 1][j - 1] + (1 if s[i - 1] == t[j - 1] else -1), T[i - 1][j] - 1, T[i][j - 1] - 1)

    for i in range(m, 0, -1):
        if M[0] < T[i][n]:
            M = (T[i][n], i, n)

    for j in range(n, 0, -1):
        if M[0] < T[m][j]:
            M = (T[m][j], m, j)

    return T, M


def semi_global_alignment(s, t):
    m    = len(s)
    n    = len(t)

    T, M = semi_global_alignment_table(s, t)
    e_d  = M[0]

    s_a  = []
    t_a  = []

    while m > M[1]:
        s_a.insert(0, s[m - 1])
        t_a.insert(0, '-')
        m -= 1

    while n > M[2]:
        s_a.insert(0, '-')
        t_a.insert(0, t[n - 1])
        n -= 1

    while m > 0 and n > 0:
        if T[m][n] == T[m - 1][n] - 1:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] - 1:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + (1 if s[m - 1] == t[n - 1] else -1):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    while m > 0:
        s_a.insert(0, s[m - 1])
        t_a.insert(0, '-')
        m -= 1

    while n > 0:
        s_a.insert(0, '-')
        t_a.insert(0, t[n - 1])
        n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)



def optimal_alignment_table(s, t, scoring, gap = -5):
    m = len(s)
    n = len(t)

    T = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        T[i][0] = gap * i

    for j in range(1, n + 1):
        T[0][j] = gap * j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[i][j] = max(T[i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], T[i - 1][j] + gap, T[i][j - 1] + gap)

    return T



def optimal_alignment(s, t, scoring, gap = -5):
    m   = len(s)
    n   = len(t)

    T   = optimal_alignment_table(s, t, scoring, gap)
    e_d = T[m][n]

    s_a = []
    t_a = []

    while m > 0 and n > 0:
        if T[m][n] == T[m - 1][n] + gap:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] + gap:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + scoring[s[m - 1]][t[n - 1]]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    while m > 0:
        s_a.insert(0, s[m - 1])
        t_a.insert(0, '-')
        m -= 1

    while n > 0:
        s_a.insert(0, '-')
        t_a.insert(0, t[n - 1])
        n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def local_alignment_table(s, t, scoring, gap = -5):
    m       = len(s)
    n       = len(t)

    table   = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    maximum = (0, 0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = max(table[i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], table[i - 1][j] + gap, table[i][j - 1] + gap, 0)
            if maximum[0] < table[i][j]:
                maximum = (table[i][j], i, j)

    return table, maximum


def local_alignment(s, t, scoring, gap = -5):
    T, M = local_alignment_table(s, t, scoring, gap)

    e_d  = M[0]
    m, n = M[1:]

    s_a  = []
    t_a  = []

    while T[m][n] > 0:
        if T[m][n] == T[m - 1][n] + gap:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] + gap:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + scoring[s[m - 1]][t[n - 1]]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def fitting_alignment_table(s, t):
    m       = len(s)
    n       = len(t)

    table   = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    maximum = (0, 0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = max(table[i - 1][j - 1] + (1 if s[i - 1] == t[j - 1] else -1), table[i - 1][j] - 1, table[i][j - 1] - 1)
            if i >= n and j >= n and maximum[0] < table[i][j]:
                maximum = (table[i][j], i, j)

    return table, maximum


def fitting_alignment(s, t):
    T, M = fitting_alignment_table(s, t)

    e_d  = M[0]
    m, n = M[1:]

    s_a  = []
    t_a  = []

    while m > 0 and n > 0:
        if T[m][n] == T[m - 1][n - 1] + (1 if s[m - 1] == t[n - 1] else -1):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1
        elif T[m][n] == T[m][n - 1] - 1:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n] - 1:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def overlap_alignment_table(s, t):
    m       = len(s)
    n       = len(t)

    table   = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    maximum = (0, 0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = max(table[i - 1][j - 1] + (1 if s[i - 1] == t[j - 1] else -2), table[i - 1][j] - 2, table[i][j - 1] - 2)

    for j in range(n, 0, -1):
        if maximum[0] < table[m][j]:
            maximum = (table[m][j], m, j)

    return table, maximum


def overlap_alignment(s, t):
    T, M = overlap_alignment_table(s, t)

    e_d  = M[0]
    m, n = M[1:]

    s_a  = []
    t_a  = []

    while n > 0:
        if T[m][n] == T[m - 1][n] - 2:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif T[m][n] == T[m][n - 1] - 2:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        elif T[m][n] == T[m - 1][n - 1] + (1 if s[m - 1] == t[n - 1] else -2):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            m -= 1
            n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)


def constant_gap_penalty_alignment_table(s, t, scoring, gap = -5):
    m = len(s)
    n = len(t)

    T = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(3)]

    for i in range(1, m + 1):
        T[0][i][0] = gap
        T[1][i][0] = gap
        T[2][i][0] = gap

    for j in range(1, n + 1):
        T[0][0][j] = gap
        T[1][0][j] = gap
        T[2][0][j] = gap

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[0][i][j] = max(T[0][i - 1][j], T[1][i - 1][j] + gap)
            T[2][i][j] = max(T[2][i][j - 1], T[1][i][j - 1] + gap)
            T[1][i][j] = max(T[0][i][j], T[1][i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], T[2][i][j])

    return T


def affine_gap_alignment_table(s, t, scoring, sigma = -11, epsilon = -1):
    m = len(s)
    n = len(t)

    T = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(3)]
    M = (0, 0, 0, 0)

    for i in range(1, m + 1):
        T[0][i][0] = sigma + (i - 1) * epsilon
        T[1][i][0] = sigma + (i - 1) * epsilon
        T[2][i][0] = sigma + (i - 1) * epsilon

    for j in range(1, n + 1):
        T[0][0][j] = sigma + (j - 1) * epsilon
        T[1][0][j] = sigma + (j - 1) * epsilon
        T[2][0][j] = sigma + (j - 1) * epsilon

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[0][i][j] = max(T[0][i - 1][j] + epsilon, T[1][i - 1][j] + sigma)
            T[2][i][j] = max(T[2][i][j - 1] + epsilon, T[1][i][j - 1] + sigma)
            T[1][i][j] = max(T[0][i][j], T[1][i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], T[2][i][j])

    for i in range(3):
        if M[0] < T[i][m][n]:
            M = (T[i][m][n], i, m, n)

    return T, M


def affine_gap_alignment(s, t, scoring, sigma = -11, epsilon = -1):
    T, M    = affine_gap_alignment_table(s, t, scoring, sigma, epsilon)

    e_d     = M[0]
    l, m, n = M[1:]

    s_a     = []
    t_a     = []

    while m > 0 and n > 0:
        if l == 0:
            if T[0][m][n] == T[1][m - 1][n] + sigma:
                l = 1
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif l == 2:
            if T[2][m][n] == T[1][m][n - 1] + sigma:
                l = 1
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        else:
            if T[1][m][n] == T[0][m][n]:
                l = 0
            elif T[1][m][n] == T[2][m][n]:
                l = 2
            else:
                s_a.insert(0, s[m - 1])
                t_a.insert(0, t[n - 1])
                m -= 1
                n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)



def affine_gap_local_alignment_table(s, t, scoring, sigma = -11, epsilon = -1):
    m       = len(s)
    n       = len(t)

    T = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(3)]
    M = (0, 0, 0, 0)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            T[0][i][j] = max(T[0][i - 1][j] + epsilon, T[1][i - 1][j] + sigma)
            T[2][i][j] = max(T[2][i][j - 1] + epsilon, T[1][i][j - 1] + sigma)
            T[1][i][j] = max(T[0][i][j], T[1][i - 1][j - 1] + scoring[s[i - 1]][t[j - 1]], T[2][i][j], 0)

            if M[0] < T[1][i][j]:
                M = (T[1][i][j], 1, i, j)

    return T, M


def affine_gap_local_alignment(s, t, scoring, sigma = -11, epsilon = -1):
    T, M    = affine_gap_local_alignment_table(s, t, scoring, sigma, epsilon)

    e_d     = M[0]
    l, m, n = M[1:]

    s_a     = []
    t_a     = []

    while T[l][m][n] > 0:

        if l == 0:
            if T[0][m][n] == T[1][m - 1][n] + sigma:
                l = 1
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            m -= 1
        elif l == 2:
            if T[2][m][n] == T[1][m][n - 1] + sigma:
                l = 1
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            n -= 1
        else:
            if T[1][m][n] == T[0][m][n]:
                l = 0
            elif T[1][m][n] == T[2][m][n]:
                l = 2
            else:
                s_a.insert(0, s[m - 1])
                t_a.insert(0, t[n - 1])
                m -= 1
                n -= 1

    return e_d, ''.join(s_a), ''.join(t_a)



def middle_column(s, t, mid, scoring, gap = -5):
    m   = len(s)
    n   = len(t)

    T   = [[0] * 2 for _ in range(m + 1)]
    B   = [(0, 0)] * (m + 1)

    for i in range(1, m + 1):
        T[i][0] = gap * i

    for j in range(1, mid + 1):
        T[0][1] = gap * j
        for i in range(1, m + 1):
            T[i][1] = max(T[i - 1][0] + scoring[s[i - 1]][t[j - 1]], T[i - 1][1] + gap, T[i][0] + gap)

            if T[i][1] == T[i - 1][0] + scoring[s[i - 1]][t[j - 1]]:
                B[i] = (1, 1)
            elif T[i][1] == T[i - 1][1] + gap:
                B[i] = (1, 0)
            elif T[i][1] == T[i][0] + gap:
                B[i] = (0, 1)

        if j < mid:
            for i in range(0, m + 1):
                T[i][0] = T[i][1]

    return [t[1] for t in T], B


def middle_node(s, t, scoring, gap = -5):
    mid = len(t) // 2
    c   = middle_column(s, t, mid, scoring, gap)[0]
    row = c.index(max(c))

    return row, mid


def middle_edge(s, t, scoring, gap = -5):
    mid  = len(t) // 2

    c    = middle_column(s, t, mid, scoring, gap)[0]
    n, b = middle_column(s[::-1], t[::-1], len(t) - mid, scoring, gap)

    n    = n[::-1]
    b    = b[::-1]

    s    = [c[i] + n[i] for i in range(len(c))]
    row  = s.index(max(s))

    off  = b[row]

    return (row, mid), (row + off[0], mid + off[1])


def calculate_score(s, t, scoring, gap = -5):
    score = 0

    for a in zip(s, t):
        if '-' in a:
            score += gap
        else:
            score += scoring[a[0]][a[1]]

    return score


def linear_space_alignment(s, t, scoring, gap = -5):

    def alignment(top, bottom, left, right):
        if right - left == 0:
            return (s[top:bottom], '-' * (bottom - top))

        if bottom - top == 0:
            return ('-' * (right - left), t[left:right])

        if right - left == 1 or bottom - top == 1:
            return optimal_alignment(s[top:bottom], t[left:right], scoring, gap)[1:]

        m, n   = middle_edge(s[top:bottom], t[left:right], scoring, gap)

        start  = alignment(top, m[0] + top, left, m[1] + left)
        middle = alignment(m[0] + top, n[0] + top, m[1] + left, n[1] + left)
        end    = alignment(n[0] + top, bottom, n[1] + left, right)

        return [start[i] + middle[i] + end[i] for i in range(2)]

    s, t  = alignment(0, len(s), 0, len(t))
    score = calculate_score(s, t, scoring, gap)
    return score, s, t







def triple_alignment_table(s, t, u):
    m = len(s)
    n = len(t)
    o = len(u)

    T = [[[0 for _ in range(o + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                T[i][j][k] = max(
                    T[i - 1][j - 1][k - 1] + (1 if (s[i - 1] == t[j - 1] == u[k - 1]) else 0), 
                    T[i - 1][j - 1][k], 
                    T[i - 1][j][k - 1], 
                    T[i][j - 1][k - 1], 
                    T[i - 1][j][k], 
                    T[i][j - 1][k], 
                    T[i][j][k - 1]
                )

    return T


def triple_alignment(s, t, u):
    m   = len(s)
    n   = len(t)
    o   = len(u)

    T   = triple_alignment_table(s, t, u)
    e_d = T[m][n][o]

    s_a = []
    t_a = []
    u_a = []

    while m > 0 and n > 0 and o > 0:
        if T[m][n][o] == T[m - 1][n - 1][o - 1] + (1 if (s[m - 1] == t[n - 1] == u[o - 1]) else 0):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            u_a.insert(0, u[o - 1])
            m -= 1
            n -= 1
            o -= 1

        elif T[m][n][o] == T[m - 1][n - 1][o]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            u_a.insert(0, '-')
            m -= 1
            n -= 1
        elif T[m][n][o] == T[m - 1][n][o - 1]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            u_a.insert(0, u[o - 1])
            m -= 1
            o -= 1
        elif T[m][n][o] == T[m][n - 1][o - 1]:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            u_a.insert(0, u[o - 1])
            n -= 1
            o -= 1

        elif T[m][n][o] == T[m - 1][n][o]:
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            u_a.insert(0, '-')
            m -= 1
        elif T[m][n][o] == T[m][n - 1][o]:
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            u_a.insert(0, '-')
            n -= 1
        elif T[m][n][o] == T[m][n][o - 1]:
            s_a.insert(0, '-')
            t_a.insert(0, '-')
            u_a.insert(0, u[o - 1])
            o -= 1



    while m > 0:
        s_a.insert(0, s[m - 1])
        m -= 1

    while n > 0:
        t_a.insert(0, t[n - 1])
        n -= 1

    while o > 0:
        u_a.insert(0, u[o - 1])
        o -= 1

    while len(s_a) < max(len(s_a), len(t_a), len(u_a)):
        s_a.insert(0, '-')

    while len(t_a) < max(len(s_a), len(t_a), len(u_a)):
        t_a.insert(0, '-')

    while len(u_a) < max(len(s_a), len(t_a), len(u_a)):
        u_a.insert(0, '-')

    return e_d, ''.join(s_a), ''.join(t_a), ''.join(u_a)







def pairwise_score(characters):
    total = 0

    for pair in combinations(characters, 2):
        total += (0 if pair[0] == pair[1] else -1)

    return total


def pairwise_scores(strings):
    total = 0

    for j in range(len(strings[0])):
        total += pairwise_score([strings[i][j] for i in range(len(strings))])

    return total







def quadruple_alignment_table(s, t, u, v):
    m = len(s)
    n = len(t)
    o = len(u)
    p = len(v)

    T = [[[[-999 for _ in range(p + 1)] for _ in range(o + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

    T[0][0][0][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                T[i][j][k][0] = pairwise_score([s[i - 1], t[j - 1], u[k - 1]]) + (i + j + k) * -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for l in range(1, p + 1):
                T[i][j][0][l] = pairwise_score([s[i - 1], t[j - 1], v[l - 1]]) + (i + j + l) * -1

    for i in range(1, m + 1):
        for k in range(1, o + 1):
            for l in range(1, p + 1):
                T[i][0][k][l] = pairwise_score([s[i - 1], u[k - 1], v[l - 1]]) + (i + k + l) * -1

    for j in range(1, n + 1):
        for k in range(1, o + 1):
            for l in range(1, p + 1):
                T[0][j][k][l] = pairwise_score([t[j - 1], u[k - 1], v[l - 1]]) + (j + k + l) * -1


    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                for l in range(1, p + 1):
                    T[i][j][k][l] = max(
                        T[i - 1][j - 1][k - 1][l - 1] + pairwise_score([s[i - 1], t[j - 1], u[k - 1], v[l - 1]]), 

                        T[i - 1][j][k][l] + pairwise_score([s[i - 1], '-', '-', '-']), 
                        T[i][j - 1][k][l] + pairwise_score(['-', t[j - 1], '-', '-']), 
                        T[i][j][k - 1][l] + pairwise_score(['-', '-', u[k - 1], '-']), 
                        T[i][j][k][l - 1] + pairwise_score(['-', '-', '-', v[l - 1]]), 

                        T[i - 1][j - 1][k][l] + pairwise_score([s[i - 1], t[j - 1], '-', '-']), 
                        T[i - 1][j][k - 1][l] + pairwise_score([s[i - 1], '-', u[k - 1], '-']), 
                        T[i - 1][j][k][l - 1] + pairwise_score([s[i - 1], '-', '-', v[l - 1]]), 
                        T[i][j - 1][k - 1][l] + pairwise_score(['-', t[j - 1], u[k - 1], '-']),
                        T[i][j - 1][k][l - 1] + pairwise_score(['-', t[j - 1], '-', v[l - 1]]), 
                        T[i][j][k - 1][l - 1] + pairwise_score(['-', '-', u[k - 1], v[l - 1]]), 

                        T[i - 1][j - 1][k - 1][l] + pairwise_score([s[i - 1], t[j - 1], u[k - 1], '-']),
                        T[i - 1][j - 1][k][l - 1] + pairwise_score([s[i - 1], t[j - 1], '-', v[l - 1]]),
                        T[i - 1][j][k - 1][l - 1] + pairwise_score([s[i - 1], '-', u[k - 1], v[l - 1]]),
                        T[i][j - 1][k - 1][l - 1] + pairwise_score(['-', t[j - 1], u[k - 1], v[l - 1]])
                    )

    return T


def quadruple_alignment(s, t, u, v):
    s   = '*' + s
    t   = '*' + t
    u   = '*' + u
    v   = '*' + v

    m   = len(s)
    n   = len(t)
    o   = len(u)
    p   = len(v)

    T   = quadruple_alignment_table(s, t, u, v)
    e_d = T[m][n][o][p]

    s_a = []
    t_a = []
    u_a = []
    v_a = []

    while m > 0 and n > 0 and o > 0 and p > 0:
        if T[m][n][o][p] == T[m - 1][n - 1][o - 1][p - 1] + pairwise_score([s[m - 1], t[n - 1], u[o - 1], v[p - 1]]):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            u_a.insert(0, u[o - 1])
            v_a.insert(0, v[p - 1])
            m -= 1
            n -= 1
            o -= 1
            p -= 1


        elif T[m][n][o][p] == T[m - 1][n - 1][o - 1][p] + pairwise_score([s[m - 1], t[n - 1], u[o - 1], '-']):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            u_a.insert(0, u[o - 1])
            v_a.insert(0, '-')
            m -= 1
            n -= 1
            o -= 1
        elif T[m][n][o][p] == T[m - 1][n - 1][o][p - 1] + pairwise_score([s[m - 1], t[n - 1], '-', v[p - 1]]):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            u_a.insert(0, '-')
            v_a.insert(0, v[p - 1])
            m -= 1
            n -= 1
            p -= 1
        elif T[m][n][o][p] == T[m - 1][n][o - 1][p - 1] + pairwise_score([s[m - 1], '-', u[o - 1], v[p - 1]]):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            u_a.insert(0, u[o - 1])
            v_a.insert(0, v[p - 1])
            m -= 1
            o -= 1
            p -= 1
        elif T[m][n][o][p] == T[m][n - 1][o - 1][p - 1] + pairwise_score(['-', t[n - 1], u[o - 1], v[p - 1]]):
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            u_a.insert(0, u[o - 1])
            v_a.insert(0, v[p - 1])
            n -= 1
            o -= 1
            p -= 1



        elif T[m][n][o][p] == T[m - 1][n - 1][o][p] + pairwise_score([s[m - 1], t[n - 1], '-', '-']):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, t[n - 1])
            u_a.insert(0, '-')
            v_a.insert(0, '-')
            m -= 1
            n -= 1
        elif T[m][n][o][p] == T[m - 1][n][o - 1][p] + pairwise_score([s[m - 1], '-', u[o - 1], '-']):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            u_a.insert(0, u[o - 1])
            v_a.insert(0, '-')
            m -= 1
            o -= 1
        elif T[m][n][o][p] == T[m - 1][n][o][p - 1] + pairwise_score([s[m - 1], '-', '-', v[p - 1]]):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            u_a.insert(0, '-')
            v_a.insert(0, v[p - 1])
            m -= 1
            p -= 1


        elif T[m][n][o][p] == T[m][n - 1][o - 1][p] + pairwise_score(['-', t[n - 1], u[o - 1], '-']):
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            u_a.insert(0, u[o - 1])
            v_a.insert(0, '-')
            n -= 1
            o -= 1
        elif T[m][n][o][p] == T[m][n - 1][o][p - 1] + pairwise_score(['-', t[n - 1], '-', v[p - 1]]):
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            u_a.insert(0, '-')
            v_a.insert(0, v[p - 1])
            n -= 1
            p -= 1
        elif T[m][n][o][p] == T[m][n][o - 1][p - 1] + pairwise_score(['-', '-', u[o - 1], v[p - 1]]):
            s_a.insert(0, '-')
            t_a.insert(0, '-')
            u_a.insert(0, u[o - 1])
            v_a.insert(0, v[p - 1])
            o -= 1
            p -= 1


        elif T[m][n][o][p] == T[m - 1][n][o][p] + pairwise_score([s[m - 1], '-', '-', '-']):
            s_a.insert(0, s[m - 1])
            t_a.insert(0, '-')
            u_a.insert(0, '-')
            v_a.insert(0, '-')
            m -= 1
        elif T[m][n][o][p] == T[m][n - 1][o][p] + pairwise_score(['-', t[n - 1], '-', '-']):
            s_a.insert(0, '-')
            t_a.insert(0, t[n - 1])
            u_a.insert(0, '-')
            v_a.insert(0, '-')
            n -= 1
        elif T[m][n][o][p] == T[m][n][o - 1][p] + pairwise_score(['-', '-', u[o - 1], '-']):
            s_a.insert(0, '-')
            t_a.insert(0, '-')
            u_a.insert(0, u[o - 1])
            v_a.insert(0, '-')
            o -= 1
        elif T[m][n][o][p] == T[m][n][o][p - 1] + pairwise_score(['-', '-', '-', v[p - 1]]):
            s_a.insert(0, '-')
            t_a.insert(0, '-')
            u_a.insert(0, '-')
            v_a.insert(0, v[p - 1])
            p -= 1




    while m > 0:
        s_a.insert(0, s[m - 1])
        m -= 1

    while n > 0:
        t_a.insert(0, t[n - 1])
        n -= 1

    while o > 0:
        u_a.insert(0, u[o - 1])
        o -= 1

    while p > 0:
        v_a.insert(0, v[p - 1])
        p -= 1



    while len(s_a) < max(len(s_a), len(t_a), len(u_a), len(v_a)):
        s_a.insert(0, '-')

    while len(t_a) < max(len(s_a), len(t_a), len(u_a), len(v_a)):
        t_a.insert(0, '-')

    while len(u_a) < max(len(s_a), len(t_a), len(u_a), len(v_a)):
        u_a.insert(0, '-')

    while len(v_a) < max(len(s_a), len(t_a), len(u_a), len(v_a)):
        v_a.insert(0, '-')



    return e_d, ''.join(s_a[1:]), ''.join(t_a[1:]), ''.join(u_a[1:]), ''.join(v_a[1:])








def failure_array(string):
    N = len(string)
    T = [0] * N

    pos = 1
    idx = 0
    while pos < N:
        if string[pos] == string[idx]:
            idx   += 1
            T[pos] = idx
            pos   += 1
        elif idx > 0:
            idx    = T[idx - 1]
        else:
            pos   += 1

    return T


def longest_subsequence(seq, increasing = True):
    sub = []

    for i in range(len(seq)):
        if increasing:
            sub.append(max([sub[j] for j in range(i) if sub[j][-1] < seq[i]] or [[]], key = len) + [seq[i]])
        else:
            sub.append(max([sub[j] for j in range(i) if sub[j][-1] > seq[i]] or [[]], key = len) + [seq[i]])

    return max(sub, key = len)


def longest_common_subsequence_table(s, t):
    m = len(s)
    n = len(t)

    C = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                C[i][j] = C[i - 1][j - 1] + 1
            else:
                C[i][j] = max(C[i][j - 1], C[i - 1][j])

    return C


def longest_common_subsequence(s, t):
    m = len(s)
    n = len(t)

    C = longest_common_subsequence_table(s, t)

    sequence = []

    while m != 0 and n != 0:
        if C[m][n] == C[m - 1][n]:
            m -= 1
        elif C[m][n] == C[m][n - 1]:
            n -= 1
        elif s[m - 1] == t[n - 1]:
            sequence.insert(0, s[m - 1])
            m -= 1
            n -= 1

    return ''.join(sequence)


'''
    this is a version of the below implementation that uses indexes
    rather than string slicing. Also, I'm going to have to start 
    refactoring code into tools.

    def shortest_supersequence(s, t, lcs):
        scs  = ''

        idxs = 0
        idxt = 0

        for char in lcs:
            while idxs < len(s) and s[idxs] != char:
                scs  += s[idxs]
                idxs += 1

            while idxt < len(t) and t[idxt] != char:
                scs  += t[idxt]
                idxt += 1

            scs  += char
            idxs += 1
            idxt += 1

        if idxs < len(s):
            scs += s[idxs:]

        if idxt < len(t):
            scs += t[idxt:]

        return scs

'''

def shortest_supersequence(s, t):
    lcs = longest_common_subsequence(s, t)
    scs = ''

    for char in lcs:
        while s and s[0] != char:
            scs  += s[0]
            s     = s[1:]

        while t and t[0] != char:
            scs  += t[0]
            t     = t[1:]

        scs  += char
        s, t  = s[1:], t[1:]

    if len(s) > 0:
        scs += s

    if len(t) > 0:
        scs += t

    return scs


def find_overlaps(s, t):
    length = min(len(s), len(t))
    total  = len(s) + len(t)

    for i in range(length):
        if s[i - length:] == t[:length - i]:
            combined = s + t[length - i:]
            return (total - len(combined), combined, [s, t])
        elif t[i - length:] == s[:length - i]:
            combined = t + s[length - i:]
            return (total - len(combined), combined, [s, t])

    return None


def shortest_superstring(strings):
    while len(strings) > 1:
        found = []

        for combination in combinations(strings, 2):
            overlap = find_overlaps(*combination)
            if overlap:
                found.append(overlap)

        joined  = max(found)
        strings = filter(lambda x: x not in joined[2], strings)
        strings.append(joined[1])

    return strings[0]


'''
    this is my original version of longest common substring. Very 
    naieve and brute force, but works perfectly. In fact, it's not 
    a little daft because it makes no assumptions about the nature 
    of the problem:

    def longest_common_substring(strings):
        strings = sorted(strings, key = len)

        string  = strings[0]
        longest = ''

        for i in range(len(string)):
            for j in range(i, len(string)):
                current = string[i:j + 1]
                if all(current in s for s in strings[1:]) and len(longest) < len(current):
                    longest = current

        return longest


    here is a better implementation that makes use of a few properties 
    of the longest common subsequence:

    def longest_common_substring(strings):
        strings = sorted(strings, key = len)

        search  = strings[0]
        length  = len(search)
        strings = strings[1:]

        for l in range(length, 0, -1):
            for s in range(length - l + 1):
                current = search[s:s + l]
                if all(current in string for string in strings):
                    return current

        return ''


    The current version makes use of binary search to reduce the problem 
    space - O(log(N) * N * K)

'''

def longest_common_substring(strings):
    strings = sorted(strings, key = len)

    string  = strings[0]
    length  = len(string)
    strings = strings[1:]

    def common_substring(l):
        for i in range(length - l + 1):
            cs = string[i:i + l + 1]
            if all(cs in s for s in strings):
                return cs
        return ''

    low     = 0
    high    = length

    while low + 1 < high:
        mid = low + (high - low) // 2
        if common_substring(mid):
            low  = mid
        else:
            high = mid

    return common_substring(low)


def interwoven_sequences(string1, string2):
    length1 = len(string1)
    length2 = len(string2)

    if length1 + length2 == 1:
        return string1 if length2 == 0 else string2

    sequences = set()

    if string1:
        for sequence in interwoven_sequences(string1[1:], string2):
            sequences.add(string1[0] + sequence)

    if string2:
        for sequence in interwoven_sequences(string1, string2[1:]):
            sequences.add(string2[0] + sequence)

    return sequences


def sequences_interweave(string, string1, string2):
    if len(string1) == 0:
        return string.startswith(string2)

    if len(string2) == 0:
        return string.startswith(string1)

    return ((string1[0] == string[0] and sequences_interweave(string[1:], string1[1:], string2)) 
        or  (string2[0] == string[0] and sequences_interweave(string[1:], string1, string2[1:])))


def interwoven_matrix(string, strings):
    lstring  = len(string)
    lstrings = len(strings)
    lall     = [len(s) for s in strings]
    M        = [[0 for i in range(lstrings)] for _ in range(lstrings)]

    for i in range(lstrings):
        for j in range(i, lstrings):
            for k in range(lstring - lall[i] - lall[j] + 1):
                if sequences_interweave(string[k:], strings[i], strings[j]):
                    M[i][j] = 1
                    M[j][i] = 1

    return M


def find_indices_of_subsequence(s, t):
    indices = []
    index   = 0

    for c in t:
        index = s.find(c, index)
        indices.append(index + 1)

    return indices


def find_indices_of_substrings(s, t):
    indices = []
    index   = 0

    while index < len(s):
        index = s.find(t, index)
        if index == -1:
            break
        indices.append(index + 1)
        index += 1

    return indices





def shortest_non_shared_substring(s1, s2):
    length   = len(s1)
    shortest = []

    for i in range(1, length):
        for j in range(length - i + 1):
            s = s1[j:j + i]
            if not s in s2 and not s in shortest:
                shortest.append(s)
        if shortest: break

    return sorted(shortest)[0]





def burrows_wheeler_transform(text):
    matrix = []

    for i in range(len(text)):
        matrix.append(text[-i:] + text[:-i])

    return ''.join(row[-1] for row in sorted(matrix))


def inverse_burrows_wheeler_transform(text):
    first = arrays.indexed_text_array(sorted(text))
    last  = arrays.indexed_text_array(text)

    row   = [first[0]]

    while len(row) < len(first):
        row.append(first[last.index(row[-1])])

    return ''.join(r[0] for r in row[1:] + row[:1])




def burrows_wheeler_matching(pattern, first, last, ltof):
    top    = 0
    bottom = len(last) - 1

    while top <= bottom:
        if pattern:
            symbol   = pattern[-1]
            pattern  = pattern[:-1]

            itop     = top
            ibottom  = bottom

            if symbol in [s[0] for s in last[top:bottom + 1]]:

                for i in range(top, bottom + 1):
                    if last[i][0] == symbol:
                        itop = i
                        break

                for i in range(bottom, top - 1, -1):
                    if last[i][0] == symbol:
                        ibottom = i
                        break

                top    = ltof[itop]
                bottom = ltof[ibottom]
            else:
                return 0
        else:
            return bottom - top + 1


def better_burrows_wheeler_matching(pattern, bwt, cm, fo):
    top    = 0
    bottom = len(bwt) - 1

    while top <= bottom:
        if pattern:
            symbol   = pattern[-1]
            pattern  = pattern[:-1]
            if symbol in bwt[top:bottom + 1]:
                top    = fo[symbol] + cm[top][symbol]
                bottom = fo[symbol] + cm[bottom + 1][symbol] - 1
            else:
                return 0
        else:
            return bottom - top + 1


def lighter_burrows_wheeler_matching(pattern, bwt, cm, fo, psa, first, last, k):
    top    = 0
    bottom = len(bwt) - 1

    def count(num, char):
        rem   = num % k
        num   = num - rem
        count = cm[num][char]

        for i in range(num, num + rem):
            if bwt[i] == char:
                count += 1

        return count

    def find_index(index):
        count   = 0
        current = last[index]

        while index not in psa:
            index   = first.index(current)
            current = last[index]
            count  += 1

        return psa[index] + count

    while top <= bottom:
        if pattern:
            symbol  = pattern[-1]
            pattern = pattern[:-1]
            if symbol in bwt[top:bottom + 1]:
                top    = fo[symbol] + count(top, symbol)
                bottom = fo[symbol] + count(bottom + 1, symbol) - 1
            else:
                return []
        else:
            return [find_index(i) for i in range(top, bottom + 1)]


def multiple_approximate_pattern_matching(d, pattern, text, bwt, cm, fo, psa, ifirst, ilast, k):
    locations = []
    length    = len(pattern)
    offset    = length // (d + 1)

    def starts():
        starts = set()
        count  = 0

        while count < d + 1:
            index  = count * offset
            sub    = pattern[index:index + offset] if count < d else pattern[index:]

            for match in lighter_burrows_wheeler_matching(sub, bwt, cm, fo, psa, ifirst, ilast, k):
                starts.add(match - (count * offset))

            count += 1

        return starts

    for start in starts():
        if distance.hamming(text[start:start + length], pattern) <= d:
            locations.append(start)

    return locations
