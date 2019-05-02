# Project Euler
# Problem 30: Digit fifth powers
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    digitFifthPowers = []
    for i in range(2, 360000):
        fifthPowSum = 0
        val = [int(k) for k in str(i)]
        for j in val:
            fifthPowSum += int(j)**5
        if fifthPowSum == i:
            digitFifthPowers.append(str(i))

    total = 0
    for i in digitFifthPowers:
        total += int(i)
    return total

if __name__ == '__main__':
    pe.runSolution(sol)
