# rosalind_afrq
'''
To model the Hardy-Weinberg principle, assume that we have a population of N
diploid individuals. If an allele is in genetic equilibrium, then because
mating is random, we may view the 2N chromosomes as receiving their alleles 
uniformly. In other words, if there are m dominant alleles, then the probability 
of a selected chromosome exhibiting the dominant allele is simply p = m / 2N

Because the first assumption of genetic equilibrium states that the population 
is so large as to be ignored, we will assume that N
is infinite, so that we only need to concern ourselves with the value of p.

Given: 
An array A for which A[k] represents the proportion of homozygous 
recessive individuals for the k-th Mendelian factor in a diploid population. 
Assume that the population is in genetic equilibrium for all factors.

Return: 
An array B having the same length as A in which B[k] represents the probability 
that a randomly selected individual carries at least one copy of the recessive 
allele for the k-th factor.

Sample Dataset
0.1 0.25 0.5

Sample Output
0.532 0.75 0.914
'''
import numpy as np

# p[k]: the proportion of the dominant allele, 
# 1 - p[k]: the proportion of the recessive allele, 
# A[k] = (1 - p[k]) ** 2 
# B[k] = 1 - p[k] ** 2 
#      = 1 - ( 1 - sqrt(A[k]) ** 2 
#      = 2 * sqrt(A[k]) - A[k]

f = lambda x: 2 * sqrt(x) - x

a = np.array(open('rosalind_afrq.txt').readline().rstrip().split()).astype(float)
out = f(a)
out.tofile('rosalind_afrq_sub.txt', sep=' ')
