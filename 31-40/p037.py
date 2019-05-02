# Project Euler
# Problem 37: Truncable primes
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    def isTruncable(n):
        '''
        Returns if prime is truncable.
        '''
        truncated_vals = []
        a = str(n)
        for i in range(len(a)):
            truncated_vals.append(int(a[i:]))
            truncated_vals.append(int(a[:i+1]))
        for n in truncated_vals:
            if not pe.isPrime(n):
                return False
        return True

    primes = [n for n in range(11,1000000) if pe.isPrime(n)]
    trunc_primes = [s for s in primes if isTruncable(s)]
    
    return sum(trunc_primes)

if __name__ == '__main__':
    pe.runSolution(sol)