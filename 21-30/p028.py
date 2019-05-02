# Project Euler
# Problem 28: Number spiral diagonals
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    # Find number of elements on the diagonal
    n = (1001-1)/2
    return int(1 + (2/3)*n*(8*n*n + 15*n + 13)) # Algebraic expression for sum of spiral's diagonals

if __name__ == '__main__':
    pe.runSolution(sol)