# Project Euler
# Problem 24: Lexicographic permutations
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    iter_list = []
    sample_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    iter_list = sorted(list(itertools.permutations(sample_digits)))

    return ''.join(str(i) for i in (iter_list[1000000-1]))

if __name__ == '__main__':
    pe.runSolution(sol)