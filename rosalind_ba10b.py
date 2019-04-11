# rosalind_ba10b
'''
Probability of an Outcome Given a Hidden Path Problem

Given: A string x (observations), followed by the alphabet Σ from which x 
was constructed, followed by a hidden path π, followed by the states States 
and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The conditional probability Pr(x|π) that string x will be emitted by 
the HMM given the hidden path π.
'''
import numpy as np

f = open('rosalind_ba10b.txt').read().rstrip().split('\n')

x = f[0]
sigma = f[2].split()
sigma = dict(zip(sigma, range(len(sigma))))
path = f[4]
states = f[6].split()
states = dict(zip(states, range(len(states))))

emission = np.array([line.rstrip().split()[1:] for line in f[9:]], dtype=float)

p_array = np.array([emission[states[i[0]], sigma[i[1]]] for i in zip(path, x)])
p = np.product(p_array)
print(p)
