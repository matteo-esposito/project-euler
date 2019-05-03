# Project Euler
# Problem 92: Square digit chains
import pe_functions as pe

def sol(): # Can improve runtime...current = 156s
    '''
    Solution to project euler problem.
    '''
    def get_digit_square(n):
        '''
        Returns the square sum of the digits composing a given positive integer.
        (i.e. 24 -> 2**2 + 4**2 -> 20, return 20)
        '''
        sum = 0
        while n:
            sum += (n % 10)**2
            n //= 10
        return sum

    count = 0
    for i in range(10000000):
        val = i
        for _ in range(100):
            val = get_digit_square(val)
            if val == 89:
                count += 1
                break

    return count

if __name__ == '__main__':
    pe.runSolution(sol)