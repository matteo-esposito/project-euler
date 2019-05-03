# Project Euler
# Problem 49: Prime permutations
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    primes = [i for i in range(1488, 10000) if pe.isPrime(i)]
    STEP = 3330
    for n in primes:
        perms = list(itertools.permutations(str(n)))
        int_perms = []
        for i in perms:
            res = ''
            for g in i:
                res += g
            int_perms.append(int(res))

        if n+STEP in int_perms and n+2*STEP in int_perms and n+STEP in primes and n+2*STEP in primes:
            return str(n) + str(n+STEP) + str(n+2*STEP)
                
if __name__ == '__main__':
    pe.runSolution(sol)