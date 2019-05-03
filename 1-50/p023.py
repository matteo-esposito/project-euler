# Project Euler
# Problem 23: Non-abundant sums
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    values = [i for i in range(1, 28123)]
    abundant_values = [i for i in range(1, 28123) if pe.isAbundant(i)]
    abundant_sums = set()
    for i in range(len(abundant_values)):
        for j in range(i, len(abundant_values)):
            temp_val = 0
            temp_val = abundant_values[i] + abundant_values[j]
            if temp_val < 28123:
                abundant_sums.add(temp_val)
    
    return sum(values) - sum(abundant_sums)

if __name__ == '__main__':
    pe.runSolution(sol)