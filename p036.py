# Project Euler
# Problem 36: Double-base palindromes
import pe_functions as pe


def sol():
    '''
    Solution to project euler problem.
    '''
    palindromeDigits = []
    for i in range(1000000):
        if str(i) == str(i)[::-1] and str(bin(i))[2:] == str(bin(i))[len(bin(i))-1:1:-1]:
            palindromeDigits.append(i)
    return sum([int(i) for i in palindromeDigits])

if __name__ == '__main__':
    pe.runSolution(sol)
