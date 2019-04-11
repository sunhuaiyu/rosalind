# rosalind_ba10c
# Viterbi algorithm: decoding the hidden Markov chain based on observed sequence
'''
Decoding Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, 
followed by the states States, transition matrix Transition, and emission 
matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: A path that maximizes the (unconditional) probability Pr(x, π) 
over all possible paths π.
'''
import numpy as np

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    for st in states:
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}
    # Run Viterbi when t > 0
    for t in range(1, len(obs)):
        V.append({})
        for st in states:
            max_tr_prob = max(V[t-1][prev_st]["prob"] * trans_p[prev_st][st] 
                                    for prev_st in states)
            for prev_st in states:
                if V[t-1][prev_st]["prob"] * trans_p[prev_st][st] == max_tr_prob:
                    max_prob = max_tr_prob * emit_p[st][obs[t]]
                    V[t][st] = {"prob": max_prob, "prev": prev_st}
                    break
    
    opt = []
    # The highest probability
    max_prob = max(value["prob"] for value in V[-1].values())
    previous = None
    # Get most probable state and its backtrack
    for st, data in V[-1].items():
        if data["prob"] == max_prob:
            opt.append(st)
            previous = st
            break
    # Follow the backtrack till the first observation
    for t in range(len(V) - 2, -1, -1):
        opt.insert(0, V[t + 1][previous]["prev"])
        previous = V[t + 1][previous]["prev"]
    
    return opt, max_prob


f = open('rosalind_ba10c.txt').read().rstrip().split('\n')
x = f[0]
alphabet = f[2].split()
alphabet = dict(zip(alphabet, range(len(alphabet))))
observations = [alphabet[i] for i in x]
states = f[4].split()
n = len(states)
states = dict(zip(range(n), states))

transition = np.array([line.rstrip().split()[1:] for line in f[7:7 + n]], dtype=float)
emission = np.array([line.rstrip().split()[1:] for line in f[9 + n:]], dtype=float)

path, p = viterbi(observations, states.keys(), [1/n] * n, transition, emission)
print(''.join([states[i] for i in path]))
