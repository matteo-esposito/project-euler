# Project Euler
# Problem 5: Smallest Multiple
import sys


def p5_sol(n):
    '''
    Sol to p5

    Args:
        n: largest factor to test
    '''
    divisors = [x for x in range(1, n+1)]
    for dividend in range(2520, sys.maxsize, n):
        if all(dividend % i == 0 for i in divisors):
            return dividend

if __name__ == '__main__':
    print(p5_sol(20))
