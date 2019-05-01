# Project Euler
# Problem 67: Maximum path sum II
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    # read in the data
    tree = []
    with open('data/p067.txt') as f:
        for line in f:
            tree.append([int(i) for i in line.rstrip('\n').split(" ")])
    
    # Go row by row recursively
    def recursiveSum(row_values, row_index):
        for i in range(len(row_values[row_index])):
            row_values[row_index][i] += max(row_values[row_index+1][i], row_values[row_index+1][i+1])
        
        # Handle recursive cases
        if len(row_values[row_index]) == 1:
            return row_values[row_index][0]
        else:
            return recursiveSum(row_values, row_index-1)
    
    return recursiveSum(tree, len(tree)-2)


if __name__ == '__main__':
    pe.runSolution(sol)