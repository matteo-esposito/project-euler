# Project Euler
# Problem 47: Distinct prime factors
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    prime_divisors = []
    distinct_primes = []
    for i in range(134000, 135000):
        prime_divisors = [d for d in pe.divisors(i) if pe.isPrime(d)]
        if len(prime_divisors) == 4:
            distinct_primes.append(i)
    return distinct_primes

if __name__ == '__main__':
    pe.runSolution(sol)