# Project Euler
# Problem 40: Champernowne's constant
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    digit_string = "0"
    for i in range(1,1000001):
        a = str(i)
        digit_string += a

    digit_list = list(digit_string)
    
    prod = 1
    for j in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        prod *= int(digit_list[j])

    return prod


if __name__ == '__main__':
    pe.runSolution(sol)