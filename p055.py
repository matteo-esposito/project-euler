# Project Euler
# Problem 55: Lychrel numbers
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    lychrel_nums = []
    for i in range(10000):
        result = i
        for _ in range(50):
            result += int(str(result)[::-1])
            if pe.isPalindrome(result):
                lychrel_nums.append(result)
                break

    return 10000 - len(lychrel_nums)
    
if __name__ == '__main__':
    pe.runSolution(sol)