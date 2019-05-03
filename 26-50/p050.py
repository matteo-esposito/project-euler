# Project Euler
# Problem 50: Consecutive prime sum
import pe_functions as pe

def sol():
    '''
    Solution to project euler problem.
    '''
    primes = [n for n in range(1000000) if pe.isPrime(n)]
    temp_sum = 0
    sums = []
    for i in primes:
        temp_sum += i
        if temp_sum >= 1000000:
            break
        sums.append(temp_sum)
    
    return max(sums)

if __name__ == '__main__':
    pe.runSolution(sol)