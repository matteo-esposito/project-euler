# Project Euler
# Problem 62: Cubic permutations
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    cubes = []
    count = 0
    n = 0
    while True:
        val = sorted(str(n**3))
        cubes.append(val)
        if cubes.count(val) == 5:
            return (cubes.index(val))**3
            break
        n += 1     
    
if __name__ == '__main__':
    pe.runSolution(sol)