# Project Euler
# Problem 38: Pandigital multiples
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    max_pan = 0
    prod_list = []
    final_list = []
    for i in range(9124, 9875):
        prod_list.append(str(i*1) + str(i*2))
        final_list += prod_list

    return max([num for num in final_list if pe.isPandigital(num)])

if __name__ == '__main__':
    pe.runSolution(sol)
