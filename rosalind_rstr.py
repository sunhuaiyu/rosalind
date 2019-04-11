# rosalind_stsr

import numpy as np


def rosalind_prob(s, A): # A must be a numpy array
    '''
	Given: A DNA string s of length at most 100 bp and 
	an array A containing at most 20 numbers between 0 and 1.

	Return: An array B having the same length as A 
	in which B[k] represents the common logarithm of the probability 
	that a random string constructed with the GC-content found 
	in A[k]  will match s exactly.
	'''	
    B = np.log10(((1-A)/2)**(s.count('A')+s.count('T')) * 
                  (A/2)**(s.count('G')+s.count('C'))).round(3)
    return B
        


def rstr(s, x, N):
	'''
	Given: A positive integer N ≤ 100000, a number x between 0 and 1, 
	and a DNA string s of length at most 10 bp.

	Return: The probability that if N random DNA strings 
	having the same length as s are constructed with GC-content x. 
	We allow for the same random string to be created more than once.
	'''
    return (1 - (1 - 10 ** rosalind_prob(s, x)) ** N) 
