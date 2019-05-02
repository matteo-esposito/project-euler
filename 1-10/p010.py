# Project Euler
# Problem 10:  Summation of primes
import pe_functions as pe


def sol():
    '''
    Solution to project euler problem.
    '''
    sum = 0
    for i in range(2000000):
        if pe.isPrime(i):
            sum += i
    return(sum)

if __name__ == '__main__':
    pe.runSolution(sol)
