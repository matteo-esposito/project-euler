# Project Euler
# Problem 12:  Highest divisible triangular number
import pe_functions as pe
import numpy as np


def sol(Limit):
    '''
    Solution to project euler problem.
    '''
    triangleNumber = 1
    for n in range(2, 1000000):
        triangleNumber += n
        if pe.numDivisors(triangleNumber) >= Limit:
            return triangleNumber
            break


if __name__ == '__main__':
    pe.runSolution(sol, 500)
