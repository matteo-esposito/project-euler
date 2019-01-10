# Project Euler
# Problem 7:  10001st prime number
import numpy as np
import sys


def isPrime(n):
    '''
    Finds whether or not an integer is prime.
    '''
    if n < 2:
        return False
    for i in range(2, int(round(np.sqrt(n))+1)):
        if n % i == 0:
            return False
    return True


def p7_sol(n):
    '''
    Sol to p7
    '''
    numberOfPrimes = 0
    prime = 1
    while numberOfPrimes <= n:
        prime += 1
        if isPrime(prime):
            numberOfPrimes += 1
    return prime

if __name__ == '__main__':
    print(p7_sol(10001))
