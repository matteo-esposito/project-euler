'''
Common and reusable functions for project euler.

projecteuler.com

Author:
    Matteo Esposito
'''
import numpy as np
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


def isPentagonal(n):
    '''
    Checks if a positive integer is pentagonal (i.e. equal to i(3i-1)/2)

    Args:
        n (int): Integer to be checked

    Returns:
        bool: Is the integer pentagonal
    '''
    for i in range(3000):
        return n == i*(3*i-1)/2


def factorial(n):
    '''
    Calculates the factorial of a positive integer.

    Args:
        n (int): number for operation

    Returns:
        Factorial.
    '''
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n


def fib(n):
    '''
    Generates a fixed number of values from the Fibonacci sequence.
    ** Non-recursive approach O(n)

    Args:
        n (int): The fibonacci number desired.

    Returns:
        Fibonacci number at position n.
    '''
    a = 1
    b = 0
    while n > 1:
        a, b = a+b, a
        n -= 1
    return a


def binary(n):
    '''
    Convert a positive integer to its binary(base-2) representation. We will
    make use of recurison and flooring division to make a concise function.

    Args:
        n (int): Base 10 integer to be converted to binary.

    Returns:
        Binary representation of provided integer (e.g. 13 => 1101)
    '''
    if n > 1:
        binary(n//2)
    print(n % 2, end="")


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
    print('Time elapsed: ({0:.{1}f}s)'.format((end-start), 4))


def isPandigital(digit):
    '''
    Checks if a positive integer is pandigital (i.e. for an n-digit number, it uses values 1 to n exactly once)

    Args:
        n (int): Integer to be checked

    Returns:
        bool: Is the integer pandigital
    '''
    # Turn digit input into list of digits
    a = digit
    b = str(digit)
    c = []
    for num in b:
        c.append(num)

    # Compare lengths of list of digits and unique digits
    if (len(np.unique(np.array(c))) == len(c) and '0' not in c):
        return True
    else:
        return False

def isPandigitalProduct(x, y):
    '''
    Checks if a product and its components form a pandigital number 1-9

    Returns:
        bool: Is the product combination pandigital (i.e. 39 x 186 = 7254 -> 123456789)
    '''
    # Turn digit input into list of digits
    p = x*y
    string = list(str(x) + str(y) + str(p))

    # Compare lengths of list of digits and unique digits
    if (len(np.unique(np.array(string))) == len(string) and sorted(string) == list('123456789')):
        return True
    else:
        return False

def isRightTriangle(x, y, z):
    '''
    Checks if 3 dimensions makeup a right triangle.

    Returns:
        bool: Are the 3 dims right triangle components?
    '''
    return z**2 == x**2 + y**2

def isAbundant(n):
    '''
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
   
    Returns:
        bool: Is n abundant?
    '''
    factor_list = []
    for i in range(1, n//2+1):
        if n % i == 0:
            factor_list.append(i)

    return sum(factor_list) > n

def isPerfect(n):
    '''
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
   
    Returns:
        bool: Is n perfect?
    '''
    factor_list = []
    for i in range(1, n//2+1):
        if n % i == 0:
            factor_list.append(i)

    return sum(factor_list) == n

def isDeficient(n):
    '''
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
   
    Returns:
        bool: Is n deficient?
    '''
    factor_list = []
    for i in range(1, n//2+1):
        if n % i == 0:
            factor_list.append(i)

    return sum(factor_list) < n
   