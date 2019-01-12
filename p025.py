# Project Euler
# Problem 25: 1000-digit Fibonacci number
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    for index in range(10000):
        val = pe.fib(index)
        if len(list(str(val))) >= 1000:
            return index

if __name__ == '__main__':
    pe.runSolution(sol)
