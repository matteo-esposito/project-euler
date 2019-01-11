'''
Common and reusable functions for project euler.

projecteuler.com

Author:
    Matteo Esposito
'''
import numpy as np
import math
import sys
import time


def isPrime(n):
    '''
    Determines if a given integer n is prime.

    Args:
        n (int): Integer that will be tested for primality.

    Returns:
        bool: True if prime, False otherwise.
    '''
    if n < 2:
        return False
    else:
        for i in range(2, int(round(np.sqrt(n))) + 1):
            if n % i == 0:
                return False
        return True


def numDivisors(value):
    '''
    Finds the number of divisors of a positive integer.

    Args:
        value (int): The integer that will be factored

    Returns:
        Number of divisors.
    '''
    numFactors = 0
    for i in range(1, int(round(np.sqrt(value))+1)):
        if value % i == 0:
            numFactors += 2
        if i**2 == value:
            numFactors -= 1
    return numFactors


def splitLongString(word, step):
    '''
    Split string by predefined step size.

    Args:
        word (str): word to be parsed and split
        step (int): cutoff index

    Returns:
        Split string.
    '''
    lambda word, step: [word[i:i+step] for i in range(0, len(word), step)]


def factorial(n):
    '''
    Returns the factorial of a number.

    Args:
        n(int): number for operation

    Returns:
        Factorial.
    '''
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n


def runSolution(func, *args):
    '''
    Run and print main program and record how long it takes to execute.

    Args:
        func: a function
        *args: argument(s) for the function provided

    Returns:
        The output of the provided function and the amount of time elapsed
        from the call of the function to the end of execution.
    '''
    start = time.clock()
    print(str(func(*args)))
    end = time.clock()
    print('Time elapsed: ' + '(' + str(end - start) + 's)')
