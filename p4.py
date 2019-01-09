# Project Euler
# Problem 4: Largest Palindrome Product
import numpy as np


def isPrime(num):
    '''
    Check if a given positive integer is a prime.

    returns:
        bool - is num prime?
    '''
    if num < 2:
        return False
    elif num % 2 == 0:
        return False
    else:
        i = 3
        while i <= int(round(np.sqrt(num))):
            if num % i == 0:
                return False
            i += 2
        return True


def p4_sol():
    '''
    Sol to p4
    '''
    NUM = 600851475143
    sum = 0
    prime_factors = []
    for i in range(1, int(round(np.sqrt(NUM)))):
        if NUM % i == 0 and isPrime(i):
            prime_factors.append(i)

    return(prime_factors[-1])

if __name__ == '__main__':
    print(p4_sol())
