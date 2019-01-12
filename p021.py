# Project Euler
# Problem 21: Amicable numbers
import pe_functions as pe
import numpy as np


def sol():
    '''
    Solution to project euler problem.
    '''
    def sumDivisors(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum

    def amicablePairs():
        sums = [sumDivisors(i) for i in range(1, 10001)]
        pairs = []
        for i in range(10000):
            index = sums[i]
            if i + 1 < index and 1 <= index
            and index <= 10000 and sums[index-1] == i + 1:
                pairs.append([i+1, index])
        return pairs

    return sum([sum(pair) for pair in amicablePairs()])

if __name__ == '__main__':
    pe.runSolution(sol)
