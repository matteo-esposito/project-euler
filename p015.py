# Project Euler
# Problem 15:  Lattice paths
import pe_functions as pe
import numpy as np


def sol(grid_size):
    '''
    Solution to project euler problem.
    '''
    grid = [1] * grid_size
    for i in range(grid_size):
        for j in range(i):
            grid[j] = grid[j] + grid[j-1]
        grid[i] = 2 * grid[i-1]
    return(grid[grid_size-1])

if __name__ == '__main__':
    pe.runSolution(sol, 20)
