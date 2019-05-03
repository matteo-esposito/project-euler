# Project Euler
# Problem 41: Pandigital prime
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    # Generate permutations of digits 1-9
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    perms = []
    perms_digits = []
    listprime = []
    for i in range(1,10):
        perms = list(itertools.permutations(digits[:i]))
        perms_digits = [(int(''.join(j))) for j in perms]
        listprime += perms_digits
    return max([num for num in listprime if pe.isPrime(num)])

if __name__ == '__main__':
    pe.runSolution(sol)
