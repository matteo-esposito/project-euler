# Project Euler
# Problem 80: Square root digital expansion
import pe_functions as pe
import numpy as np

def sol():
    '''
    Solution to project euler problem.
    '''
    def isIrrational(n):
        '''
        Check if root of n is an integer, if not, then it's root is irrational.
        '''
        return np.sqrt(n) - int(np.sqrt(n)) != 0

    # Use BigInteger class in java to get decimal precision desired
    root = 0
    decimal_sum = 0
    values = []
    int_values = []
    for i in range(101):
        if isIrrational(i):
            root = list(str(np.sqrt(i)))
            decimal = root.index('.')
            values = root[decimal+1:decimal+1+100]
            int_values = [int(i) for i in values]
            decimal_sum += sum(int_values)
    return decimal_sum

if __name__ == '__main__':
    pe.runSolution(sol)