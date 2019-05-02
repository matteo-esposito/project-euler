# Project Euler
# Problem 44: Pentagon numbers
import pe_functions as pe
import numpy as np

def sol():
    '''
    Solution to project euler problem.
    '''
    def isPentagonal(n):
        r = np.sqrt(1+24*n)
        return r % 6 == 5

    dvals = []
    d = 0
    s = 0
    
    for j in range(1, 3000):
        pj = j*(3*j-1)/2
        for k in range(j, 3000):
            pk = k*(3*k-1)/2
            d = pk - pj
            s = pk + pj
            if isPentagonal(d) and isPentagonal(s):
                dvals.append(abs(d))
    return int(min(dvals))

if __name__ == '__main__':
    pe.runSolution(sol)