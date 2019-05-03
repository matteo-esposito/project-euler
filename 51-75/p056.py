# Project Euler
# Problem 56: Powerful digit sum
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    val = 0
    val_list = []
    sums = []
    for a in range(50, 100):
        for b in range(50, 100):
            val_list.append(a**b)

    for n in val_list:
        temp_val = 0
        for d in str(n):
            temp_val += int(d)
        sums.append(temp_val)
            
    return max(sums)

if __name__ == '__main__':
    pe.runSolution(sol)