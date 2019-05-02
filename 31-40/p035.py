# Project Euler
# Problem 33: Circular primes
import pe_functions as pe
import itertools

def sol():
    '''
    Solution to project euler problem.
    '''
    def rotate(string, n):
        '''
        Returns rotated string, shifted by n positions
        '''
        return string[n:] + string[:n]

    def isCircular(n):
        '''
        Returns true if all permutations of a given prime are also prime.
        '''
        a = []        
        for i in range(len(str(n))):
            a.append(int(rotate(str(n), i)))

        for val in a:
            if not pe.isPrime(val):
                return False
        return True
    
    primes = [n for n in range(2,1000000) if pe.isPrime(n)]
    circular_values = [i for i in primes if isCircular(i)]
    
    return len(circular_values)

if __name__ == '__main__':
    pe.runSolution(sol)