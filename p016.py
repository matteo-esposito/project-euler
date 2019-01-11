# Project Euler
# Problem 16: Power digit sum
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    val = list(str(2**1000))
    return(sum([int(i) for i in val]))

if __name__ == '__main__':
    pe.runSolution(sol)
