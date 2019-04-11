# rosalind_ba10a
'''
Probability of a Hidden Path Problem

Given: A hidden path π followed by the states States and transition matrix 
Transition of an HMM (Σ, States, Transition, Emission).

Return: The probability of this path, Pr(π). You may assume that initial 
probabilities are equal.
'''
import numpy as np

f = open('rosalind_ba10a.txt')
s = f.readline().rstrip()
_b = f.readline()
states = f.readline().rstrip().split()
_b = f.readline()
_b = f.readline()

m = np.array([line.rstrip().split()[1:] for line in f], dtype=float)

states = dict(zip(states, range(len(states))))
 
path = np.array([m[states[i[0]], states[i[1]]] for i in zip(s[:-1], s[1:])])
p = 1/len(states) * np.product(path)

print(p)
