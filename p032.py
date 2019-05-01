# Project Euler
# Problem 32: Pandigital products
import pe_functions as pe
import numpy as np
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    prod_list = []
    prod_list = [x*y for x in range(1, 100) for y in range(100, 10000) if pe.isPandigitalProduct(x, y)]
    return sum(np.unique(np.array(prod_list)))

if __name__ == '__main__':
    pe.runSolution(sol) 
