# Project Euler
# Problem 33: Digit cancelling fractions
import pe_functions as pe
import math

def sol():
    '''
    Solution to project euler problem.
    '''
    nprod = 1
    dprod = 1 
    
    for i in range(1, 10):
        for d in range(1, i):
            for n in range(1, d):
                if d*(10*n + i) == n*(i*10 + d):
                    dprod *= d 
                    nprod *= n 
    dprod /= math.gcd(nprod, dprod)
    return int(dprod)

if __name__ == '__main__':
    pe.runSolution(sol)