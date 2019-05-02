# Project Euler
# Problem 46: Goldbach's other conjecture
import pe_functions as pe
import numpy as np

def sol():
    '''
    Solution to project euler problem.
    '''
    primes = [i for i in range(2, 10000) if pe.isPrime(i)]
    notprimes = [j for j in range(2, 10000) if not pe.isPrime(j)]
    goldbach_nums = []
    for i in primes:
        for k in range(100):
            goldbach_nums.append(int(i + 2*k*k))

    bad_set = []
    for n in notprimes:
        if n not in goldbach_nums and n % 2 != 0:
            bad_set.append(n)
    
    return min(bad_set)

if __name__ == '__main__':
    pe.runSolution(sol)