# Project Euler
# Problem 26: Reciprocal cycles
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    def find_cycle(d):
        '''
        Return the length of the repeating portion of the decimal
        representation of 1/d where d is a positive integer.
        '''
        remainder = 10
        i = 0
        while remainder != 10 or i < 1:
            remainder = (remainder % d)*10
            i += 1 
        return i

    longest_cycle = 0
    current_cycle = 0
    max_d = 0
    sample_set = [i for i in range(2,1000) if i % 2 != 0 and i % 5 != 0 and pe.isPrime(i)]
    for i in sample_set:
        current_cycle = find_cycle(i)
        if current_cycle > longest_cycle:
            longest_cycle = current_cycle
            max_d = i
    return max_d

if __name__ == '__main__':
    pe.runSolution(sol)