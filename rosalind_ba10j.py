# rosalind_ba10j
'''
Soft Decoding Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, 
followed by the states States, transition matrix Transition, and 
emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The probability Pr(πi = k|x) that the HMM was in state k at step i 
(for each state k and each step i).
'''
import numpy as np
from pandas import DataFrame


def forward_backward(Y, states, A, B):
    '''Given: A observation sequence Y (1...t...T), the states set X (1...i...N),  
    and transition matrix A and emission matrix B of an HMM.
    Return: The probability Pr(πi = k|Y) that the HMM was in state k at step t 
    (for each state k and each step i).'''

    n = len(Y)          # n-length observations
    m = len(states)     # m states
    init_state_p = 1.0 / m  # assuming equal initial probabilities of all states
    
    # initialize forward and backward score table
    V_f = np.zeros(shape=(m, n), dtype=float)
    V_b = V_f.copy()

    # forward
    V_f[:, 0] = init_state_p * B[:, Y[0]]
    for t in range(n-1):
        V_f[:, t+1] = B[:, Y[t+1]] * (V_f[:, t].dot(A)) 
            
    # backward
    V_b[:, -1] = 1.0
    for t in range(n-2, -1, -1):
        V_b[:, t] = A.dot(V_b[:, t+1] * B[:, Y[t+1]])
    
    return V_f * V_b


f = open('rosalind_ba10j.txt').read().rstrip().split('\n--------\n')
alphabet = f[1].split()
alphabet_num = list(range(len(alphabet)))
alphabet_dict = dict(zip(alphabet, alphabet_num))
X = [alphabet_dict[i] for i in f[0]]   #observation sequence
states = f[2].split()
states_num = list(range(len(states)))

T = np.array([line.split()[1:] for line in f[3].split('\n')[1:]], dtype=float)
E = np.array([line.split()[1:] for line in f[4].split('\n')[1:]], dtype=float)

result = forward_backward(X, list(range(len(states))), T, E)
result = (result / result.sum(0)).round(4).T
DataFrame(result, columns=states).to_csv('rosalind_ba10j_sub.txt', sep='\t', index=0)
