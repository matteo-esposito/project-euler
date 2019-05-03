# Project Euler
# Problem 20:  Factorial digit sum
import pe_functions as pe
import numpy as np


def sol(n):
    '''
    Solution to project euler problem.
    '''
    digits = list(str(pe.factorial(n)))
    return (sum([int(i) for i in digits]))

if __name__ == '__main__':
    pe.runSolution(sol, 100)
