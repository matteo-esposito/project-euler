# Project Euler
# Problem 29: Distinct powers
import pe_functions as pe


def sol():
    '''
    Solution to project euler problem.
    '''
    distinctPowers = []
    for a in range(2, 101):
        for b in range(2, 101):
            distinctPowers.append(a**b)
    return len(set(distinctPowers))


if __name__ == '__main__':
    pe.runSolution(sol)
