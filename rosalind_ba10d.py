# rosalind_ba10d
'''
Outcome Likelihood Problem ("Forward Procedure")

Given: A string x, followed by the alphabet Σ from which x was constructed, 
followed by the states States, transition matrix Transition, 
and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The probability Pr(x) that the HMM emits x.
'''
import numpy as np

def hmm_forward(x, A, B, n):
    '''the probability of a observed sequence, given HMM parameters --
    A: transition matrix; B: emission matrix; n: number of states'''
    alpha = np.array([1./n] * n, float) * B[:, x[0]]

    for t in x[1:]:
        alpha = alpha.dot(A) * B[:, t]

    return sum(alpha)

def hmm_forward2(x, A, B, n):
    '''the probability of a observed sequence, given HMM parameters --
    A: transition matrix; B: emission matrix; n: number of states'''
    alpha = [np.array([1./n] * n, float) * B[:, x[0]]]

    for t in x[1:]:
        alpha.append(alpha[-1].dot(A) * B[:, t])

    return alpha

f = open('rosalind_ba10d.txt').read().rstrip().split('\n')
x = f[0]
alphabet = f[2].split()
alphabet = dict(zip(alphabet, range(len(alphabet))))
x = [alphabet[i] for i in x] #translate observation vector into index vector of alphabet
states = f[4].split()
n = len(states)
 
# transition matrix
A = np.array([line.rstrip().split()[1:] for line in f[7:7 + n]], float)
# emission matrix
B = np.array([line.rstrip().split()[1:] for line in f[9 + n:]], float)
    
print(hmm_forward(x, A, B, n))
