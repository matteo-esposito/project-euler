# Project Euler
# Problem 39: Integer right triangles
import pe_functions as pe
import numpy as np

def sol():
    '''
    Solution to project euler problem.
    '''
    max_perim = 0
    max_sols = 0
    for p in range(141, 1000):
        num_sols = 0
        for a in range(100, p//2):
            for b in range(100, p//2):
                if pe.isRightTriangle(a, b, p-a-b):
                    num_sols += 1
        if num_sols > max_sols:
            max_perim, max_sols = p, num_sols

    return max_perim


if __name__ == '__main__':
    pe.runSolution(sol) 
