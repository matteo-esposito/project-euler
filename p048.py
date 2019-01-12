# Project Euler
# Problem 48: Self powers
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    series = 0
    for i in range(1, 1001):
        series += i**i
    return str(series)[-10:]

if __name__ == '__main__':
    pe.runSolution(sol)
