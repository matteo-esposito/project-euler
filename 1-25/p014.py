# Project Euler
# Problem 14:  Largest Collatz sequence
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    def generateCollatz(n, count=1):
        while n > 1:
            count += 1
            if n % 2 == 0:
                n = n/2
            else:
                n = 3*n+1
        return count

    maxVal = 1
    maxLen = 0
    for i in range(1000000):
        currLen = generateCollatz(i)
        if currLen > maxLen:
            maxLen = currLen
            maxVal = i

    return(maxVal)

if __name__ == '__main__':
    pe.runSolution(sol)
