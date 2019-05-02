# Project Euler
# Problem 53: Combinatoric selections
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    def choose(n, r):
        return (pe.factorial(n))/(pe.factorial(r)*pe.factorial(n-r))
    
    count = 0
    for n in range(1, 101):
        for r in range(1, n):
            if choose(n, r) > 1000000:
                count += 1
    return count


if __name__ == '__main__':
    pe.runSolution(sol)