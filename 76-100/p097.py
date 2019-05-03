# Project Euler
# Problem 97: Large non-Mersenne prime
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    # Basically we are only performing the operation on the last 10 digits and 
    # omitting the larger power values.
    n = 2
    for i in range(7830456):
        n = 2*n % 10000000000

    n *= 28433
    n += 1

    return n % 10000000000

if __name__ == '__main__':
    pe.runSolution(sol)