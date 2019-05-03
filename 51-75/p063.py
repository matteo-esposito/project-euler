# Project Euler
# Problem 63: Powerful digit counts
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    power_count = 0
    for x in range(1,30):
        for n in range(1,30):
            if len(str(x**n)) == n:
                power_count += 1
    return power_count

if __name__ == '__main__':
    pe.runSolution(sol)