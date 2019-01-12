# Project Euler
# Problem 34: Digit factorials
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    digitFactorials = []
    for i in range(3, 1000000):
        factorialSum = 0
        val = [int(k) for k in str(i)]
        for j in val:
            factorialSum += pe.factorial(int(j))
        if factorialSum == i:
            digitFactorials.append(str(i))

    total = 0
    for i in digitFactorials:
        total += int(i)
    return total

if __name__ == '__main__':
    pe.runSolution(sol)
