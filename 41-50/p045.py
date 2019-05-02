# Project Euler
# Problem 45: Triangular, pentagonal, and hexagonal
import pe_functions as pe
import numpy as np

def sol():
    '''
    Solution to project euler problem.
    '''
    def isPentagonal(n):
        r = np.sqrt(1+24*n)
        return r % 6 == 5

    def isTriangle(n):
        r = np.sqrt(1+8*n)
        return r % 2 == 1

    def isHexagonal(n):
        r = np.sqrt(1+8*n)
        return r % 4 == 3

    pent = [j*(3*j-1)/2 for j in range(50000,300000)]
    tri = [j*(j+1)/2 for j in range(50000,300000)]
    hexa = [j*(2*j-1) for j in range(50000,300000)]

    for n in tri:
        if isPentagonal(n) and isHexagonal(n):
            ans = int(n)
            break
    return ans

if __name__ == '__main__':
    pe.runSolution(sol)