# Project Euler
# Problem 27: Quadratic primes
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    def count_consecutive_primes(a, b):
        '''
        Finds the number of consecutive primes generated by 
        y = n^2 + an + b.
        '''
        fx = 0
        for n in range(100000):
            fx = n*n + a*n + b
            if not pe.isPrime(fx):
                return n

    temp_count = 0
    max_count = 0
    max_val = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000):
            temp_count = count_consecutive_primes(a, b)
            if temp_count > max_count:
                max_count = temp_count
                max_val = a*b
    return max_val

if __name__ == '__main__':
    pe.runSolution(sol)