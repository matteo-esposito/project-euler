# Project Euler
# Problem 11:  Largest product in a grid
import pe_functions as pe
import numpy as np

data = np.genfromtxt('data/p011.txt', delimiter=" ", dtype=np.int32)


def sol():
    '''
    Solution to project euler problem.
    '''
    def getVerticalProd(i, j):
        return(np.prod([sub[j] for sub in data[i:i+4]]))

    def getHorizontalProd(i, j):
        return(np.prod(data[i][j:j+4]))

    def getUpperDiagProd(i, j):
        if i <= 2 or j >= 17:
            return 0

        upperProdVals = []
        for a, b in zip(range(i, i-4, -1), range(j, j+4)):
            upperProdVals.append(data[a][b])
        return(np.prod(upperProdVals))

    def getLowerDiagProd(i, j):
        if i >= 17 or j >= 17:
            return 0

        lowerProdVals = []
        for a, b in zip(range(i, i+4), range(j, j+4)):
            lowerProdVals.append(data[a][b])
        return(np.prod(lowerProdVals))

    p_max = 0
    for row_ind, rows in enumerate(data):
        for col_ind, _ in enumerate(rows):
            p1 = getVerticalProd(row_ind, col_ind)
            p2 = getHorizontalProd(row_ind, col_ind)
            p3 = getUpperDiagProd(row_ind, col_ind)
            p4 = getLowerDiagProd(row_ind, col_ind)
            if p1 > p_max:
                p_max = p1
            elif p2 > p_max:
                p_max = p2
            elif p3 > p_max:
                p_max = p3
            elif p4 > p_max:
                p_max = p4
    return(p_max)


if __name__ == '__main__':
    pe.runSolution(sol)
